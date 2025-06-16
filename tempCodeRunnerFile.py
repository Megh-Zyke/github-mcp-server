from github import Github
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    """Function used to compare the two mentioned commits in a repository. The response needs to be sufficiently detailed with respect to the changes made in the two commits. """
    g = Github(os.getenv("GITHUB_TOKEN_1"))
    try:
        repository = g.get_repo("Megh-Zyke/AI-teammate-for-Codebase-Insights")
        commits = repository.get_commits()
        print("Total number of commits:", commits.totalCount)
        print()
        
        diff = repository.compare(commits.sha[-1], commits.sha[-2])
        changes = []
        
        for file_diff in diff.files:
            changes.append({
                "filename": file_diff.filename,
                "status": file_diff.status,
                "changes": file_diff.patch
            })
        
        return f"Comparison between {commit1} and {commit2}:\n" + "\n".join([f"{change['filename']} ({change['status']}): {change['changes']}" for change in changes])
    except Exception as e:
        return f"Error comparing commits: {str(e)}"



if __name__ == "__main__":
    print(main())
