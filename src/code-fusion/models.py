import os
import argparse
from typing import Dict, List
from rich.console import Console

console = Console()

models_cheap: Dict[str, str] = {
    "google": "gemini/gemini-1.5-flash",
    "anthropic": "anthropic/claude-3-haiku-20240307",
    "openai": "openai/gpt-4o-mini",
    "meta": "openrouter/meta-llama/llama-3.1-8b-instruct",
}

models_best: Dict[str, str] = {
    "google": "gemini/gemini-1.5-pro-latest",
    "anthropic": "anthropic/claude-3-5-sonnet-20240620",
    "openai": "openai/gpt-4o",
    "meta": "openrouter/meta-llama/llama-3.1-405b-instruct"
}

def parse_arguments():
    parser = argparse.ArgumentParser(description="CodeFusion: Compare responses from multiple AI models")
    parser.add_argument("--best", action="store_true", help="Use the best (more expensive) models")
    return parser.parse_args()

args = parse_arguments()

def select_models() -> List[str]:
    available_models = list(models_best.keys() if args.best else models_cheap.keys())
    model_type = "best" if args.best else "cheap"
    console.print(f"Available {model_type} models: [cyan]{', '.join(available_models)}[/cyan]")

    selected_models: List[str] = []
    while len(selected_models) < 2:
        user_input = console.input("Enter at least two models you want to use (space-separated): ").lower()
        selected_models = [model.strip() for model in user_input.replace(",", " ").split() if model.strip() in available_models]
        if len(selected_models) < 2:
            console.print(f"[red]Please select at least two valid models from: {', '.join(available_models)}[/red]")
    return selected_models

def setup_api_keys(selected_models: List[str]) -> None:
    model_to_env: Dict[str, str] = {
        "@": "GEMINI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
        "openai": "OPENAI_API_KEY",
        "meta": "OPENROUTER_API_KEY",
    }

    for model in selected_models:
        env_var = model_to_env[model]
        if not os.getenv(env_var):
            key = console.input(f"Enter your {model.capitalize()} API key: ").strip()
            os.environ[env_var] = key
        else:
            console.print(f"[green]{model.capitalize()} API key found in environment variables.[/green]")

def get_model_id(model_name: str) -> str:
    return models_best[model_name] if args.best else models_cheap[model_name]