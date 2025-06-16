from github import Github
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    g = Github(os.getenv("GITHUB_TOKEN"))
    try:
        repository = g.get_repo("Megh-Zyke/Efficiency-Benchmark")
        return f"Repository: {repository.name}, Stars: {repository.stargazers_count}, Forks: {repository.forks_count}"
    except Exception as e:
        return f"Error fetching repository info: {str(e)}"


if __name__ == "__main__":
    print(main())
