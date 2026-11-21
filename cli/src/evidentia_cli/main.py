import typer
from evidentia_cli.client import APIClientError, EvidentiaClient
from evidentia_cli.config import get_settings
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="evidentia",
    help="Evidence-grounded AI research assistant.",
    no_args_is_help=True,
)
console = Console()
err_console = Console(stderr=True)


def get_client() -> EvidentiaClient:
    settings = get_settings()
    return EvidentiaClient(
        base_url=settings.app_url,
        timeout=settings.timeout,
    )


def handle_error(exc: APIClientError):
    err_console.print(f"[red]Error:[/red] {exc}")
    raise typer.Exit(code=1) from exc


@app.command()
def health():
    """Check whether the Evidentia API is responding."""
    try:
        with get_client() as client:
            response = client.health()
    except APIClientError as exc:
        handle_error(exc)
        return
    console.print(f"API status: [green]{response.status}[/green]")


@app.command()
def info():
    """Display Evidentia API information."""
    try:
        with get_client() as client:
            response = client.info()
    except APIClientError as exc:
        handle_error(exc)
        return
    table = Table(title="Evidentia API")
    table.add_column("Property")
    table.add_column("Value")
    table.add_row("Name", response.name)
    table.add_row("Version", response.version)
    console.print(table)
