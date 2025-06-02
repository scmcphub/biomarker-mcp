import asyncio
import pytest
from fastmcp import Client
import anndata
from pathlib import Path

import nest_asyncio
nest_asyncio.apply()


@pytest.mark.asyncio 
async def test_query_celltype_marker(mcp):
    """Test listing available CCC methods."""
    async with Client(mcp) as client:
        result = await client.call_tool("db_query_celltype_marker", {
            "request":{
                "species": ["Human"], 
                "tissue_class": ["Pancreas"]},
        })
        assert "Pancreas" in result[0].text
