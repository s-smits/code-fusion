import asyncio
import logging
from typing import Dict, List, AsyncGenerator
from litellm import acompletion
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout

console = Console()

async def query_model(model_name: str, model_id: str, messages: List[Dict[str, str]], max_retries: int = 3) -> AsyncGenerator[str, None]:
    for attempt in range(max_retries):
        try:
            response = await acompletion(model=model_id, messages=messages, stream=True)
            
            async for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    yield content
            return
        except Exception as e:
            if attempt < max_retries - 1:
                console.print(f"[yellow]Retrying {model_name} (attempt {attempt + 2}/{max_retries})...[/yellow]")
                await asyncio.sleep(1)
            else:
                error_message = f"Error querying {model_name}: {str(e)}"
                logging.error(error_message)
                console.print(f"[red]{error_message}[/red]")
                return

async def display_concurrent_responses(model_generators, model_names):
    responses = [""] * len(model_generators)
    done = [False] * len(model_generators)

    def generate_layout():
        layout = Layout()
        layout.split_column(*[Layout(name=model) for model in model_names])
        for i, model in enumerate(model_names):
            layout[model].update(Panel(
                responses[i],
                title=f"{model.upper()} RESPONSE",
                border_style="cyan",
                expand=True
            ))
        return layout

    with Live(generate_layout(), refresh_per_second=10, vertical_overflow="visible") as live:
        while not all(done):
            for i, gen in enumerate(model_generators):
                if not done[i]:
                    try:
                        chunk = await anext(gen)
                        responses[i] += chunk
                    except StopAsyncIteration:
                        done[i] = True
                    except Exception as e:
                        responses[i] += f"\nError: {str(e)}"
                        done[i] = True
            live.update(generate_layout())
            await asyncio.sleep(0.05)

    # Print full responses after live update
    console.print("\n[bold cyan]Full Responses:[/bold cyan]")
    for model, response in zip(model_names, responses):
        console.print(f"\n[bold]{model.upper()} RESPONSE:[/bold]")
        console.print(Panel(response, border_style="cyan", expand=True))

    return responses

async def process_query(user_query, selected_models, get_model_id):
    console.print(f"[yellow]Querying models...[/yellow]")
    
    model_generators = [query_model(model_name, get_model_id(model_name), [{"role": "user", "content": user_query}]) 
                        for model_name in selected_models]
    
    responses = await display_concurrent_responses(model_generators, selected_models)
    
    return dict(zip(selected_models, responses))

async def summarize_responses(user_query, responses):
    summary_prompt = f"Analyze the following query and responses from different AI models:\n\nUser Query: {user_query}\n\n"
    for model, response in responses.items():
        summary_prompt += f"{model.capitalize()} Response:\n{response}\n\n"
    summary_prompt += "Please summarize the similarities and differences between these responses CONCISELY. "
    summary_prompt += "Focus on the key points, approach, and any notable variations in the answers provided. "
    summary_prompt += "Finally, provide a swift recommendation (10 words) on which model to choose and why."

    try:
        summary_response = await acompletion(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": summary_prompt}],
            stream=True
        )

        console.print("\n[magenta]SUMMARY:[/magenta]")
        summary = ""
        async for chunk in summary_response:
            content = chunk.choices[0].delta.content
            if content:
                console.print(content, end="")
                summary += content
        console.print("\n")
        return summary
    except Exception as e:
        error_message = f"Error generating summary: {str(e)}"
        logging.error(error_message)
        console.print(f"[red]{error_message}[/red]")
        return None