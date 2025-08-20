import pytest


@pytest.fixture
def mcp():
    from biomarker_mcp.server import db_mcp

    return db_mcp
