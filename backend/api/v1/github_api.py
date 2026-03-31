from fastapi import APIRouter, Depends, Path
from typing import List, Any
from controller.github_controller import GithubController
from models import SuccessResponse, CreateIssueRequest, CreatePullRequestRequest, CreateBranchRequest, CreateFileRequest

router = APIRouter()

@router.get("/repos", response_model=SuccessResponse[List[Any]])
async def list_repositories(controller: GithubController = Depends()):
    """Fetch all your repositories automatically."""
    return await controller.get_repos()

@router.post("/issues", response_model=SuccessResponse[dict])
async def create_issue(
    request_data: CreateIssueRequest,
    controller: GithubController = Depends()
):
    """Create Issue"""
    return await controller.create_issue(request_data)

@router.get("/issues/{repo}", response_model=SuccessResponse[List[Any]])
async def list_issues(
    repo: str = Path(..., description="The name of your repository"),
    controller: GithubController = Depends()
):
    """List issues in your repository."""
    return await controller.list_issues(repo)

@router.get("/commits/{repo}", response_model=SuccessResponse[List[Any]])
async def list_commits(
    repo: str = Path(..., description="The name of your repository"),
    controller: GithubController = Depends()
):
    """Fetch commit history for your repository."""
    return await controller.get_commits(repo)

@router.post("/create-branch", response_model=SuccessResponse[dict])
async def create_branch(
    request_data: CreateBranchRequest,
    controller: GithubController = Depends()
):
    """Create a new branch from a base branch."""
    return await controller.create_branch(request_data)

@router.post("/create-file", response_model=SuccessResponse[dict])
async def create_file(
    request_data: CreateFileRequest,
    controller: GithubController = Depends()
):
    """Push a new file to a specific branch."""
    return await controller.create_file(request_data)

@router.post("/create-pull-request", response_model=SuccessResponse[dict])
async def create_pull_request(
    request_data: CreatePullRequestRequest,
    controller: GithubController = Depends()
):
    """Create Pull Request"""
    return await controller.create_pull_request(request_data)
