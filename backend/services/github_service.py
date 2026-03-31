import httpx
import base64
from utils.context import get_current_user_login
from models.github_model import CreateIssueRequest, CreatePullRequestRequest
from config import settings

class GithubService:
    def __init__(self, token: str, client: httpx.AsyncClient):
        self.token = token
        self.client = client
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": settings.GITHUB_ACCEPT_HEADER,
        }

    async def get_repositories(self) -> httpx.Response:
        """Raw GET call for repositories."""
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/user/repos", 
            headers=self.headers
        )

    async def create_issue(self, data: CreateIssueRequest) -> httpx.Response:
        """Raw POST call for issue creation."""
        owner = get_current_user_login()
        payload = data.model_dump(exclude={"repo"}, exclude_none=True)
        return await self.client.post(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{data.repo}/issues",
            headers=self.headers,
            json=payload
        )

    async def list_issues(self, repo: str) -> httpx.Response:
        """Raw GET call for issue listing."""
        owner = get_current_user_login()
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/issues",
            headers=self.headers
        )

    async def get_commits(self, repo: str) -> httpx.Response:
        """Raw GET call for commit history."""
        owner = get_current_user_login()
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/commits",
            headers=self.headers
        )

    async def create_pull_request(self, data: CreatePullRequestRequest) -> httpx.Response:
        """Raw POST call for pull request creation."""
        owner = get_current_user_login()
        payload = data.model_dump(exclude={"repo"}, exclude_none=True)
        return await self.client.post(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{data.repo}/pulls",
            headers=self.headers,
            json=payload
        )

    async def get_branch_sha(self, repo: str, branch: str) -> httpx.Response:
        """Fetch the SHA of a specific branch."""
        owner = get_current_user_login()
        return await self.client.get(
            f"{settings.GITHUB_BASE_URL}/repos/{owner}/{repo}/git/ref/heads/{branch}",
            headers=self.headers
        )

    async def create_branch(self, repo: str, new_branch: str, sha: str) -> httpx.Response:
        """Create a new branch reference."""
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
        """Create or update a file in a repository."""
        owner = get_current_user_login()
        # GitHub requires base64 encoding for file content
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