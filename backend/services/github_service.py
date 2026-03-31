import httpx
import base64
from utils.context import get_current_user_login
from models.github_model import CreateIssueRequest, CreatePullRequestRequest
from config import settings

class GithubService:
    """
    GithubService handles direct low-level communication with the GitHub REST API.
    It encapsulates header management and endpoint orchestration.
    """
    def __init__(self, token: str, client: httpx.AsyncClient):
        """
        Initializes the service with a verified GitHub token and a shared HTTP client.
        """
        self.token = token
        self.client = client
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": settings.GITHUB_ACCEPT_HEADER,
        }

    async def get_repositories(self) -> httpx.Response:
        """
        Lists repositories for the currently authenticated user.
        """
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/user/repos", 
            headers=self.headers
        )

    async def create_issue(self, data: CreateIssueRequest) -> httpx.Response:
        """
        Creates a new issue in the specified repository.
        Uses the 'repo' field to determine the target repository 
        and excludes it from the payload.
        """
        owner = get_current_user_login()
        payload = data.model_dump(exclude={"repo"}, exclude_none=True)
        return await self.client.post(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{data.repo}/issues",
            headers=self.headers,
            json=payload
        )

    async def list_issues(self, repo: str) -> httpx.Response:
        """
        Retrieves a list of issues for the specified repository owner and name.
        """
        owner = get_current_user_login()
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/issues",
            headers=self.headers
        )

    async def get_commits(self, repo: str) -> httpx.Response:
        """
        Fetches the commit history for a specific repository.
        """
        owner = get_current_user_login()
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/commits",
            headers=self.headers
        )

    async def create_pull_request(self, data: CreatePullRequestRequest) -> httpx.Response:
        """
        Creates a Pull Request between two branches.
        The targets (owner/repo) are derived from the current user context 
        and request data.
        """
        owner = get_current_user_login()
        payload = data.model_dump(exclude={"repo"}, exclude_none=True)
        return await self.client.post(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{data.repo}/pulls",
            headers=self.headers,
            json=payload
        )

    async def get_branch_sha(self, repo: str, branch: str) -> httpx.Response:
        """
        Retrieves the Git SHA for a specific branch reference.
        This is typically used as a base SHA for creating new branches.
        """
        owner = get_current_user_login()
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/git/ref/heads/{branch}",
            headers=self.headers
        )

    async def create_branch(self, repo: str, new_branch: str, sha: str) -> httpx.Response:
        """
        Creates a new Git reference (branch) at a specific commit SHA.
        """
        owner = get_current_user_login()
        payload = {
            "ref": f"refs/heads/{new_branch}",
            "sha": sha
        }
        return await self.client.post(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/git/refs",
            headers=self.headers,
            json=payload
        )

    async def create_file(self, repo: str, branch: str, path: str, content: str) -> httpx.Response:
        """
        Creates or updates a file at a specific path within a branch.
        Note: GitHub requires the file content to be Base64 encoded.
        """
        owner = get_current_user_login()
        # Encode content to Base64 as required by GitHub API
        encoded_content = base64.b64encode(content.encode()).decode()
        payload = {
            "message": f"Create {path} via API Test Setup",
            "content": encoded_content,
            "branch": branch
        }
        return await self.client.put(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/contents/{path}",
            headers=self.headers,
            json=payload
        )