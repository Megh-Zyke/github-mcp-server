import os
from github import Github
from mcp.server.fastmcp import FastMCP

from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("GitHub")

@mcp.tool()
def get_repo_info(repo: str) -> str:
    """Fetches the repository information for a given repository name."""
    g = Github(os.getenv("GITHUB_TOKEN"))
    try:
        repository = g.get_repo(repo)
        return f"Repository: {repository.name}, Stars: {repository.stargazers_count}, Forks: {repository.forks_count}"
    except Exception as e:
        return f"Error fetching repository info: {str(e)}"
    

@mcp.tool()
def get_total_number_of_commits(repo: str) -> int :
    """Fetches the total number of commits for a given repository name."""
    g = Github(os.getenv("GITHUB_TOKEN"))
    try:
        repository = g.get_repo(repo)
        return repository.get_commits().totalCount
    except Exception as e:
        return f"Error fetching total number of commits: {str(e)}"


                         


if __name__ == "__main__":
    # The transport is set to "stdio" for standard input/output to receive and respond to tool function calls.
    mcp.run(transport="stdio")
    
    