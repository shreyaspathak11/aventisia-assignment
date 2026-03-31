from fastapi import Depends
from httpx import HTTPStatusError
from typing import List, Any

from api.deps import get_github_service
from services import GithubService
from models import SuccessResponse, CreateIssueRequest, CreatePullRequestRequest, CreateBranchRequest, CreateFileRequest
from utils.errors import handle_api_error

class GithubController:
    """
    GithubController orchestrates high-level business logic for GitHub operations.
    It coordinates requests to the GithubService and handles error transformation 
    for the API layer.
    """
    def __init__(self, service: GithubService = Depends(get_github_service)):
        """
        Initializes the controller with an injected GithubService.
        """
        self.github_service = service

    async def get_repos(self) -> SuccessResponse[List[Any]]:
        """
        Retrieves a list of all repositories for the authenticated user.
        Raises an HTTPException via handle_api_error on failure.
        """
        try:
            response = await self.github_service.get_repositories()
            response.raise_for_status()
            return SuccessResponse(message="Repositories fetched successfully", data=response.json())
        except Exception as e:
            handle_api_error(e, "Failed to fetch repositories")

    async def create_issue(self, data: CreateIssueRequest) -> SuccessResponse[dict]:
        """
        Orchestrates the creation of a new issue in a GitHub repository.
        """
        try:
            response = await self.github_service.create_issue(data)
            response.raise_for_status()
            return SuccessResponse(message="Issue created successfully", data=response.json())
        except Exception as e:
            handle_api_error(e, "Failed to create issue")

    async def list_issues(self, repo: str) -> SuccessResponse[List[Any]]:
        """
        Retrieves all issues associated with a specific repository.
        """
        try:
            response = await self.github_service.list_issues(repo)
            response.raise_for_status()
            return SuccessResponse(message="Issues listed successfully", data=response.json())
        except Exception as e:
            handle_api_error(e, "Failed to list issues")

    async def get_commits(self, repo: str) -> SuccessResponse[List[Any]]:
        """
        Retrieves the commit timeline and metadata for a repository.
        """
        try:
            response = await self.github_service.get_commits(repo)
            response.raise_for_status()
            return SuccessResponse(message="Commits fetched successfully", data=response.json())
        except Exception as e:
            handle_api_error(e, "Failed to fetch commits")

    async def create_branch(self, data: CreateBranchRequest) -> SuccessResponse[dict]:
        """
        Atomically creates a new branch.
        First retrieves the 'latest commit' SHA from a base branch,
        then creates a new reference pointing to that SHA.
        """
        try:
            # 1. Retrieve current state (SHA) of the base branch
            sha_resp = await self.github_service.get_branch_sha(data.repo, data.base_branch)
            sha_resp.raise_for_status()
            sha = sha_resp.json()["object"]["sha"]

            # 2. Create the new branch reference
            branch_resp = await self.github_service.create_branch(data.repo, data.branch_name, sha)
            branch_resp.raise_for_status()

            return SuccessResponse(
                message=f"Branch '{data.branch_name}' created successfully",
                data=branch_resp.json()
            )
        except Exception as e:
            handle_api_error(e, "Failed to create branch")

    async def create_file(self, data: CreateFileRequest) -> SuccessResponse[dict]:
        """
        Directly pushes a file to the specified repository and branch.
        """
        try:
            file_resp = await self.github_service.create_file(
                data.repo, 
                data.branch_name, 
                data.path, 
                data.content
            )
            file_resp.raise_for_status()

            return SuccessResponse(
                message=f"File '{data.path}' pushed successfully",
                data=file_resp.json()
            )
        except Exception as e:
            handle_api_error(e, "Failed to push file")
            
    async def create_pull_request(self, data: CreatePullRequestRequest) -> SuccessResponse[dict]:
        """
        Initializes a new Pull Request on GitHub based on the provided head and base branches.
        """
        try:
            response = await self.github_service.create_pull_request(data)
            response.raise_for_status()
            return SuccessResponse(message="Pull request created successfully", data=response.json())
        except Exception as e:
            handle_api_error(e, "Failed to create pull request")