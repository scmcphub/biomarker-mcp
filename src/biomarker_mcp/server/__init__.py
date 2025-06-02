from scmcp_shared.server import BaseMCPManager

from .celltype import db_mcp

class BiomarkerMCPManager(BaseMCPManager):
    """Manager class for Biomarker MCP modules."""
    
    def _init_modules(self):
        """Initialize available Biomarker MCP modules."""
        self.available_modules = {
            "db": db_mcp,
        }
