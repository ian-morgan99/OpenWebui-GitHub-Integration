"""Request Models for API Endpoints"""
from typing import List, Optional

from pydantic import BaseModel, Field


class RepositoryAnalysisRequest(BaseModel):
    """Request model for repository health analysis."""

    repo_owner: str = Field(..., description="Repository owner username or organization")
    repo_name: str = Field(..., description="Repository name")
    token: str = Field(..., description="GitHub personal access token")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "repo_owner": "octocat",
                    "repo_name": "Hello-World",
                    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                }
            ]
        }
    }


class IssueCreateRequest(BaseModel):
    """Request model for creating an issue."""

    repo_owner: str = Field(..., description="Repository owner")
    repo_name: str = Field(..., description="Repository name")
    title: str = Field(..., description="Issue title", min_length=1, max_length=256)
    body: Optional[str] = Field(None, description="Issue body/description")
    labels: Optional[List[str]] = Field(default=None, description="List of label names")
    assignees: Optional[List[str]] = Field(default=None, description="List of usernames to assign")
    token: str = Field(..., description="GitHub personal access token")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "repo_owner": "octocat",
                    "repo_name": "Hello-World",
                    "title": "Bug: Application crashes on startup",
                    "body": "## Description\n\nThe application crashes when...",
                    "labels": ["bug", "critical"],
                    "assignees": ["octocat"],
                    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                }
            ]
        }
    }


class PRCreateRequest(BaseModel):
    """Request model for creating a pull request."""

    repo_owner: str = Field(..., description="Repository owner")
    repo_name: str = Field(..., description="Repository name")
    title: str = Field(..., description="Pull request title", min_length=1, max_length=256)
    body: Optional[str] = Field(None, description="Pull request body/description")
    head: str = Field(..., description="The name of the branch where your changes are implemented")
    base: str = Field(..., description="The name of the branch you want the changes pulled into")
    draft: bool = Field(default=False, description="Create as draft PR")
    token: str = Field(..., description="GitHub personal access token")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "repo_owner": "octocat",
                    "repo_name": "Hello-World",
                    "title": "Add new feature",
                    "body": "## Changes\n\n- Added feature X\n- Fixed bug Y",
                    "head": "feature-branch",
                    "base": "main",
                    "draft": False,
                    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                }
            ]
        }
    }


class ReleaseCreateRequest(BaseModel):
    """Request model for creating a release."""

    repo_owner: str = Field(..., description="Repository owner")
    repo_name: str = Field(..., description="Repository name")
    tag_name: str = Field(..., description="The name of the tag")
    name: Optional[str] = Field(None, description="The name of the release")
    body: Optional[str] = Field(None, description="Release notes")
    draft: bool = Field(default=False, description="Create as draft release")
    prerelease: bool = Field(default=False, description="Mark as pre-release")
    token: str = Field(..., description="GitHub personal access token")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "repo_owner": "octocat",
                    "repo_name": "Hello-World",
                    "tag_name": "v1.0.0",
                    "name": "Version 1.0.0",
                    "body": "## What's Changed\n\n- Feature 1\n- Feature 2",
                    "draft": False,
                    "prerelease": False,
                    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                }
            ]
        }
    }
