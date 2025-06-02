
import pytest

@pytest.fixture
def mcp():
    from biomarker_mcp.server import BiomarkerMCPManager
    return BiomarkerMCPManager("biomarker-mcp").mcp