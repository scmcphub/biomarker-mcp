from fastmcp import FastMCP, Context
from fastmcp.exceptions import ToolError
from ..schema.celltype import CellMarkerDB
import importlib.resources as pkg_resources
import pandas as pd
import os
from datetime import datetime

db_mcp = FastMCP("BioMarkerMCP-DB-Server")


@db_mcp.tool()
def query_celltype_marker(request: CellMarkerDB, ctx: Context):
    """query the celltype marker from cellmarker database"""
    try:
        with pkg_resources.path("biomarker_mcp.data", "Cell_marker_All.csv") as db_file:
            if not os.path.exists(db_file):
                raise FileNotFoundError(f"Database file not found at {db_file}")
            db_df: pd.DataFrame = pd.read_csv(db_file)
    except Exception as e:
        raise ToolError(f"Failed to load database: {str(e)}")

    # Apply filters based on provided fields
    if request.species:
        db_df = db_df.loc[db_df["species"].isin(request.species)]

    if request.tissue_class:
        db_df = db_df.loc[db_df["tissue_class"].isin(request.tissue_class)]

    if request.tissue_type:
        db_df = db_df.loc[db_df["tissue_type"].isin(request.tissue_type)]

    if request.cancer_type:
        cancer_types = db_df["cancer_type"].unique()
        db_df = db_df.loc[db_df["cancer_type"].isin(request.cancer_type)]
        if len(db_df) == 0:
            return f"404 NOT FOUND ERROR: No records found for cancer_type: {request.cancer_type}, available cancer_types: {cancer_types}"

    if request.cell_type:
        db_df = db_df.loc[db_df["cell_type"].isin(request.cell_type)]

    if request.cell_name:
        cellnames = db_df.loc[:, "cell_name"].unique()
        db_df = db_df.loc[db_df["cell_name"].isin(request.cell_name)]
        if len(db_df) == 0:
            return f"404 NOT FOUND ERROR: No records found for cell_name: {request.cell_name}, available cell_names: {cellnames}"

    if request.Symbol:
        db_df = db_df.loc[db_df["Symbol"].isin(request.Symbol)]

    if request.Genetype:
        db_df = db_df.loc[db_df["Genetype"].isin(request.Genetype)]

    if request.GeneID:
        db_df = db_df.loc[db_df["GeneID"].isin(request.GeneID)]

    # Get filtered results
    result = db_df.loc[:, request.show_columns].head(request.show_num)

    # Create output directory if it doesn't exist
    output_dir = "query_results"
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cellmarker_query_{timestamp}.csv"
    output_path = os.path.join(output_dir, filename)

    # Write results to CSV file
    db_df.loc[:, request.show_columns].to_csv(output_path, index=False)

    return {
        "total_records_number": len(result),
        f"show_{request.show_num}_records": str(result),
        "full_records_output_file": output_path,
    }
