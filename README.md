# GitHub MCP Server

A Model Context Protocol (MCP) server implementation for GitHub, enabling AI agents and LLMs to interact with GitHub repositories programmatically via standardized JSON-RPC tools.

---

## Overview

This MCP server provides access to key GitHub repository features via a set of tools, including:

* Retrieving repository metadata (stars, forks, etc.)
* Querying commits and comparing commits
* Managing GitHub issues: listing, creating, commenting, labeling, assigning, and closing

By exposing these functions over MCP, any MCP-compatible client or large language model (LLM) can seamlessly use GitHub as a contextual data source and tool.

---

## Features

| Tool Name                     | Description                                       |
| ----------------------------- | ------------------------------------------------- |
| `get_repo_info`               | Fetch basic repository info (stars, forks, name)  |
| `get_total_number_of_commits` | Get the total number of commits in a repository   |
| `get_commit_numbers`          | List commit SHA hashes                            |
| `get_commit_details`          | Retrieve details about a specific commit          |
| `compare_commits`             | Compare two commits and return file-level changes |
| `get_all_issues`              | List all issues with details                      |
| `get_issue_by_number`         | Get details of a specific issue                   |
| `create_issue`                | Create a new issue                                |
| `comment_on_issue`            | Add a comment to an issue                         |
| `get_issue_comments`          | Retrieve all comments on an issue                 |
| `add_issue_labels`            | Add labels to an issue                            |
| `remove_issue_labels`         | Remove labels from an issue                       |
| `assign_issue`                | Assign users to an issue                          |
| `unassign_issue`              | Remove assignees from an issue                    |
| `close_issue`                 | Close an issue                                    |

---

## Setup and Usage

### Prerequisites

* Python 3.8+
* GitHub Personal Access Token (PAT) with repo and issue scopes
* [FastMCP](https://pypi.org/project/mcp-server-fastmcp/)
* `PyGithub` library
* `python-dotenv` for environment variable management

### Installation

1. Clone the repository (or create your own project).

2. Install dependencies:

```bash
pip install PyGithub python-dotenv mcp-server-fastmcp
```

3. Create a `.env` file with your GitHub token:

```
GITHUB_TOKEN_1=your_personal_access_token_here
```

4. Run the MCP server:

```bash
python github_mcp_server.py
```

This will start the MCP server listening on standard input/output (stdio) by default.

---

## Authentication

This server uses a GitHub Personal Access Token loaded from the environment variable `GITHUB_TOKEN_1`. Make sure the token has sufficient permissions to read repositories and manage issues.

---

## How It Works

* Each tool function is decorated with `@mcp.tool()` to expose it via MCP.
* The server listens for JSON-RPC requests from an MCP client.
* On receiving a request, it calls the appropriate tool and returns the result.
* Errors during API calls are returned as error strings (future versions will improve error handling).

---

## Future Improvements

* Structured JSON responses for better LLM parsing
* Enhanced error handling with MCP-standard errors
* Permission and rate limit handling
* Expanded GitHub API coverage: pull requests, branches, contributors
* OAuth-based authentication flows

---
