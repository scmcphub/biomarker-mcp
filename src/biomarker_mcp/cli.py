"""
Command-line interface for biomarker-mcp.

This module provides a CLI entry point for the biomarker-mcp package.
"""

import os
from enum import Enum

import typer

from .server import db_mcp

app = typer.Typer(
    name="biomarker-mcp",
    help="Biomarker MCP Server CLI",
    add_completion=False,
    no_args_is_help=True,  # Show help if no args provided
)


class Transport(str, Enum):
    STDIO = "stdio"
    SSE = "sse"
    SHTTP = "shttp"


@app.command(name="run")
def run(
    transport: Transport = typer.Option(
        Transport.STDIO,
        "-t",
        "--transport",
        help="Specify transport type",
        case_sensitive=False,
    ),
    port: int = typer.Option(8000, "-p", "--port", help="transport port"),
    host: str = typer.Option("127.0.0.1", "--host", help="transport host"),
):
    """Start Biomarker MCP Server"""
    # Set environment variables
    os.environ["BIO_TRANSPORT"] = transport.value
    os.environ["BIO_HOST"] = host
    os.environ["BIO_PORT"] = str(port)

    if transport == Transport.STDIO:
        db_mcp.run()
    elif transport == Transport.SSE:
        db_mcp.run(transport="sse", host=host, port=port, log_level="info")
    elif transport == Transport.SHTTP:
        db_mcp.run(transport="streamable-http", host=host, port=port, log_level="info")


@app.callback()
def main():
    """Abcoder MCP CLI root command."""
    pass
