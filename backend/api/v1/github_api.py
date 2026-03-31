from fastapi import APIRouter, Depends, Path
from typing import List, Any
from controller.github_controller import GithubController
from models import SuccessResponse, CreateIssueRequest, CreatePullRequestRequest, CreateBranchRequest, CreateFileRequest

router = APIRouter()

@router.get("/repos", response_model=SuccessResponse[List[Any]])
async def list_repositories(controller: GithubController = Depends()):
    """
    Retrieves all repositories associated with the authenticated GitHub user.
    """
    return await controller.get_repos()

@router.post("/issues", response_model=SuccessResponse[dict])
async def create_issue(
    request_data: CreateIssueRequest,
    controller: GithubController = Depends()
):
    """
    Creates a new issue in the repository specified in the request body.
    """
    return await controller.create_issue(request_data)

@router.get("/issues/{repo}", response_model=SuccessResponse[List[Any]])
async def list_issues(
    repo: str = Path(..., description="The name of your repository"),
    controller: GithubController = Depends()
):
    """
    Lists all issues for a specific repository.
    The repository name must be provided as a URL path parameter.
    """
    return await controller.list_issues(repo)

@router.get("/commits/{repo}", response_model=SuccessResponse[List[Any]])
async def list_commits(
    repo: str = Path(..., description="The name of your repository"),
    controller: GithubController = Depends()
):
    """
    Fetches the commit history and metadata for a specific repository.
    """
    return await controller.get_commits(repo)

@router.post("/create-branch", response_model=SuccessResponse[dict])
async def create_branch(
    request_data: CreateBranchRequest,
    controller: GithubController = Depends()
):
    """
    Creates a new branch on GitHub using a specified base branch as the source.
    """
    return await controller.create_branch(request_data)

@router.post("/create-file", response_model=SuccessResponse[dict])
async def create_file(
    request_data: CreateFileRequest,
    controller: GithubController = Depends()
):
    """
    Commits a new file with specified content to a specific repository and branch.
    Handles the internal Base64 encoding required by GitHub.
    """
    return await controller.create_file(request_data)

@router.post("/create-pull-request", response_model=SuccessResponse[dict])
async def create_pull_request(
    request_data: CreatePullRequestRequest,
    controller: GithubController = Depends()
):
    """
    Initializes a new Pull Request on GitHub.
    """
    return await controller.create_pull_request(request_data)
