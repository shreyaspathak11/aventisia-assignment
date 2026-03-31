from pydantic import BaseModel, Field
from typing import Optional

class CreateIssueRequest(BaseModel):
    """Schema for creating a new issue in your own repository."""
    repo: str = Field(..., description="The name of your repository")
    title: str = Field(..., description="The title of the issue")
    body: Optional[str] = Field(None, description="The detailed description of the issue")

class CreateBranchRequest(BaseModel):
    """Schema for creating a new branch."""
    repo: str = Field(..., description="The name of your repository")
    branch_name: str = Field(..., description="The name of the new branch to create")
    base_branch: str = Field(default="main", description="The branch to fork from")

class CreateFileRequest(BaseModel):
    """Schema for pushing a new file."""
    repo: str = Field(..., description="The name of your repository")
    branch_name: str = Field(..., description="The branch to push the file to")
    path: str = Field(..., description="The file path (e.g., 'test-api.txt')")
    content: str = Field(..., description="The file content")

class CreatePullRequestRequest(BaseModel):
    """Schema for creating a new pull request in your own repository."""
    repo: str = Field(..., description="The name of your repository")
    title: str = Field(..., description="The title of the pull request")
    head: str = Field(..., description="The name of the branch with changes")
    base: str = Field(default="main", description="The target branch")
    body: Optional[str] = Field(None, description="The detailed description of the pull request")