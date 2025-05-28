from mcp.server.fastmcp import FastMCP
from backstage_api import BackstageApiWrapper
import os

BACKSTAGE_TOKEN = os.getenv("BACKSTAGE_TOKEN")
BACKSTAGE_URL = os.getenv("BACKSTAGE_URL", "http://localhost:7007/")
api_wrapper = BackstageApiWrapper(token=BACKSTAGE_TOKEN, base_url=BACKSTAGE_URL)

mcp = FastMCP("Backstage TechDocs MCP")

@mcp.tool()
def search_techdocs(query: str):
    return api_wrapper.get_techdocs_search_results(query)

