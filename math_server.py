from mcp.server.fastmcp import FastMCP

# Create FastMCP instance
mcp = FastMCP("Math")

# Override the default server settings to set a new port
mcp.settings.port = 8001  # ✅ Force FastMCP to use port 8001 instead of 8000

# Define MCP Tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    # ✅ Start MCP Server on Port 8001
    mcp.run(transport="sse")
