import asyncio
from dotenv import load_dotenv
from rich.console import Console
from models import select_models, setup_api_keys, get_model_id
from query_processing import process_query, summarize_responses
import logging
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Configure logging
logging.getLogger("litellm").setLevel(logging.ERROR)
logging.getLogger("litellm.llms").setLevel(logging.ERROR)
logging.getLogger("litellm.utils").setLevel(logging.ERROR)

console = Console()

async def main_async() -> None:
    console.print("[green]Welcome to CodeFusion![/green]")

    selected_models = select_models()
    setup_api_keys(selected_models)

    try:
        while True:
            user_query = console.input("[yellow]Enter your programming query (or 'quit' to exit): [/yellow]").strip()
            
            if user_query.lower() == 'quit':
                console.print("[green]Exiting the program.[/green]")
                break
            
            if user_query:
                responses = await process_query(user_query, selected_models, get_model_id)
                console.print("\n[yellow]Generating summary...[/yellow]")
                await summarize_responses(user_query, responses)
            else:
                console.print("[red]Please enter a valid query.[/red]")
    except KeyboardInterrupt:
        console.print("\n[yellow]Program interrupted. Exiting.[/yellow]")
    except Exception as e:
        logging.error(f"An error occurred in the main loop: {str(e)}", exc_info=True)
        console.print("[red]An unexpected error occurred. Please check the logs for more information.[/red]")

def main() -> None:
    load_dotenv()  # Load environment variables from .env file
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    asyncio.run(main_async())

if __name__ == "__main__":
    main()