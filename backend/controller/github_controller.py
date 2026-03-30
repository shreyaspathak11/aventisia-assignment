from fastapi import HTTPException, Depends
from httpx import HTTPStatusError
from typing import List, Any

from api.deps import get_github_service
from services import GithubService
from models import SuccessResponse, CreateIssueRequest, CreatePullRequestRequest
from utils.logger import logger

class GithubController:
    def __init__(self, service: GithubService = Depends(get_github_service)):
        """
        The Controller now manages its own dependency on the Service.
        This keeps the API routes extremely clean.
        """
        self.github_service = service

    async def get_repos(self) -> SuccessResponse[List[Any]]:
        """List all your repositories."""
        try:
            response = await self.github_service.get_repositories()
            response.raise_for_status()
            return SuccessResponse(message="Repositories fetched successfully", data=response.json())
        except HTTPStatusError as e:
            logger.error(f"GitHub Error: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch repositories")
        except Exception as e:
            logger.error(f"System Error: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal Server Error during GitHub communication")

    async def create_issue(self, data: CreateIssueRequest) -> SuccessResponse[dict]:
        """Create a new issue."""
        try:
            response = await self.github_service.create_issue(data)
            response.raise_for_status()
            return SuccessResponse(message="Issue created successfully", data=response.json())
        except HTTPStatusError as e:
            logger.error(f"GitHub Error: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail="Failed to create issue")
        except Exception as e:
            logger.error(f"System Error: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to proceed with issue creation")

    async def list_issues(self, repo: str) -> SuccessResponse[List[Any]]:
        """List issues for a repository."""
        try:
            response = await self.github_service.list_issues(repo)
            response.raise_for_status()
            return SuccessResponse(message="Issues listed successfully", data=response.json())
        except HTTPStatusError as e:
            logger.error(f"GitHub Error: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail="Failed to list issues")
        except Exception as e:
            logger.error(f"System Error: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to fetch issues list")

    async def get_commits(self, repo: str) -> SuccessResponse[List[Any]]:
        """Fetch commits history."""
        try:
            response = await self.github_service.get_commits(repo)
            response.raise_for_status()
            return SuccessResponse(message="Commits fetched successfully", data=response.json())
        except HTTPStatusError as e:
            logger.error(f"GitHub Error: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch commits")
        except Exception as e:
            logger.error(f"System Error: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to fetch commit history")

    async def create_pull_request(self, data: CreatePullRequestRequest) -> SuccessResponse[dict]:
        """Create a new pull request."""
        try:
            response = await self.github_service.create_pull_request(data)
            response.raise_for_status()
            return SuccessResponse(message="Pull request created successfully", data=response.json())
        except HTTPStatusError as e:
            logger.error(f"GitHub Error: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail="Failed to create pull request")
        except Exception as e:
            logger.error(f"System Error: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to proceed with pull request")
