from pydantic import BaseModel, Field
from typing import Optional

class CreateIssueRequest(BaseModel):
    """Schema for creating a new issue in your own repository."""
    repo: str = Field(..., description="The name of your repository")
    title: str = Field(..., description="The title of the issue")
    body: Optional[str] = Field(None, description="The detailed description of the issue")

class CreatePullRequestRequest(BaseModel):
    """Schema for creating a new pull request in your own repository."""
    repo: str = Field(..., description="The name of your repository")
    title: str = Field(..., description="The title of the pull request")
    head: str = Field(..., description="The name of the branch with changes")
    base: str = Field(default="main", description="The target branch")
    body: Optional[str] = Field(None, description="The detailed description of the pull request")