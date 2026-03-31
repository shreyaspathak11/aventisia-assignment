from pydantic import BaseModel, Field
from typing import Optional

class CreateIssueRequest(BaseModel):
    """
    Data model for the 'Create Issue' request.
    Encapsulates the repository, title, and body for the issue creation.
    """
    repo: str = Field(..., description="The name of the target repository")
    title: str = Field(..., description="The title for the new issue")
    body: Optional[str] = Field(None, description="The descriptive body text for the issue")

class CreateBranchRequest(BaseModel):
    """
    Data model for creating a new Git branch reference.
    """
    repo: str = Field(..., description="The target repository name")
    branch_name: str = Field(..., description="The name of the new branch to be created")
    base_branch: str = Field(default="main", description="The source branch SHA to fork from")

class CreateFileRequest(BaseModel):
    """
    Data model for pushing a single file to a specific repository branch.
    """
    repo: str = Field(..., description="The name of the target repository")
    branch_name: str = Field(..., description="The branch name to receive the new file")
    path: str = Field(..., description="The file path relative to the repo root")
    content: str = Field(..., description="Total file content (before Base64 encoding)")

class CreatePullRequestRequest(BaseModel):
    """
    Data model for initiating a new Pull Request on GitHub.
    """
    repo: str = Field(..., description="The repository where the pull request will be created")
    title: str = Field(..., description="The title of the proposed pull request")
    head: str = Field(..., description="The branch containing the proposed changes")
    base: str = Field(default="main", description="The branch to merge into")
    body: Optional[str] = Field(None, description="The detailed description of the pull request changes")