"""
Command-line interface for biomarker-mcp.

This module provides a CLI entry point for the biomarker-mcp package.
"""
from scmcp_shared.cli import MCPCLI
from .server import BiomarkerMCPManager

cli = MCPCLI(
    name="biomarker-mcp", 
    help_text="Biomarker MCP Server CLI",
    manager=BiomarkerMCPManager
)
