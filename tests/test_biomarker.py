import nest_asyncio
import pytest
from fastmcp import Client

nest_asyncio.apply()


@pytest.mark.asyncio
async def test_query_cancer_celltype_marker(mcp):
    """Test listing available CCC methods."""
    async with Client(mcp) as client:
        result = await client.call_tool(
            "query_cancer_celltype_marker",
            {
                "request": {"species": ["Human"], "cancer_type": ["Breast cancer"]},
            },
        )
        assert "Breast cancer" in result.content[0].text


@pytest.mark.asyncio
async def test_query_normal_celltype_marker(mcp):
    """Test listing available CCC methods."""
    async with Client(mcp) as client:
        result = await client.call_tool(
            "query_normal_celltype_marker",
            {
                "request": {"species": "Homo sapiens", "sample_type": "Tissue"},
            },
        )
        assert "Tissue" in result.content[0].text
