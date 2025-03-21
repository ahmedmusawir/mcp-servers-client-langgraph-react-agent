# import sys
# print(sys.path)
from mcp.server.fastmcp import FastMCP

# test_server.py
try:
    import mcp
    print("mcp imported successfully")
    print("mcp Server Started in stdio Mode...")
except ImportError:
    print("mcp import failed")

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")