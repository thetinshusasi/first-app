#!/usr/bin/env python3
"""
Main application entry point for first-app.
"""

import click
import requests
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import sys
from pathlib import Path

console = Console()


def get_project_info():
    """Get information about the current project."""
    project_root = Path(__file__).parent.parent
    pyproject_file = project_root / "pyproject.toml"
    
    if pyproject_file.exists():
        return {
            "name": "first-app",
            "version": "0.1.0",
            "description": "A Python project with virtual environment and TOML configuration"
        }
    return None


@click.group()
@click.version_option(version="0.1.0", prog_name="first-app")
def main():
    """First App - A Python project with virtual environment and TOML configuration."""
    pass


@main.command()
def info():
    """Display project information."""
    project_info = get_project_info()
    
    if project_info:
        table = Table(title="Project Information")
        table.add_column("Property", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        
        table.add_row("Name", project_info["name"])
        table.add_row("Version", project_info["version"])
        table.add_row("Description", project_info["description"])
        table.add_row("Python Version", f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        
        console.print(table)
    else:
        console.print("[red]Could not find project information[/red]")


@main.command()
@click.option("--url", default="https://httpbin.org/json", help="URL to fetch data from")
def fetch(url):
    """Fetch data from a URL and display it."""
    try:
        console.print(f"[yellow]Fetching data from: {url}[/yellow]")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Create a panel with the response
        text = Text(str(data), style="green")
        panel = Panel(text, title="Response Data", border_style="blue")
        console.print(panel)
        
    except requests.RequestException as e:
        console.print(f"[red]Error fetching data: {e}[/red]")
    except ValueError as e:
        console.print(f"[red]Error parsing JSON: {e}[/red]")


@main.command()
def hello():
    """Display a welcome message."""
    welcome_text = Text("Welcome to First App! 🚀", style="bold green")
    subtitle = Text("A Python project with virtual environment and TOML configuration", style="italic blue")
    
    panel = Panel(
        welcome_text + "\n\n" + subtitle,
        title="First App",
        border_style="green",
        padding=(1, 2)
    )
    console.print(panel)


if __name__ == "__main__":
    main() 