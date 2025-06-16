from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Fetches the current weather for a given location."""
    # Simulating a weather fetch operation
    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    # The transport is set to "stdio" for standard input/output to receive and respond to tool function calls.
    mcp.run(transport="streamable-http")