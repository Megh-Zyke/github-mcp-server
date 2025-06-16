from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Maths")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two integers."""
    return a * b    

# The transport is set to "stdio" for standard input/output to receive and respond to tool function calls.

if __name__ == "__main__":
    mcp.run(transport = "stdio")
    