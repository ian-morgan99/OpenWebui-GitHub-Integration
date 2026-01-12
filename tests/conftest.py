"""Pytest Configuration and Fixtures"""
import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def test_client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def mock_github_client():
    """Mock GitHub client for testing."""
    # TODO: Implement mock GitHub client
    class MockGitHubClient:
        async def get_repo(self, owner: str, repo: str):
            return {
                "name": repo,
                "full_name": f"{owner}/{repo}",
                "description": "Test repository",
                "stars": 100,
                "forks": 50,
            }

        async def create_issue(self, owner: str, repo: str, title: str, **kwargs):
            return {
                "number": 1,
                "title": title,
                "state": "open",
            }

    return MockGitHubClient()


@pytest.fixture
def mock_redis():
    """Mock Redis client for testing."""
    # TODO: Implement mock Redis client
    class MockRedis:
        def __init__(self):
            self.storage = {}

        async def get(self, key: str):
            return self.storage.get(key)

        async def set(self, key: str, value: str, ex: int = None):
            self.storage[key] = value
            return True

        async def delete(self, key: str):
            if key in self.storage:
                del self.storage[key]
            return True

    return MockRedis()


@pytest.fixture
def sample_repository():
    """Sample repository data for testing."""
    return {
        "id": 123456,
        "name": "test-repo",
        "full_name": "octocat/test-repo",
        "owner": {
            "login": "octocat",
            "type": "User",
        },
        "description": "A test repository",
        "private": False,
        "fork": False,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-10T00:00:00Z",
        "pushed_at": "2024-01-10T00:00:00Z",
        "size": 1024,
        "stargazers_count": 100,
        "watchers_count": 100,
        "language": "Python",
        "forks_count": 50,
        "open_issues_count": 10,
        "default_branch": "main",
    }


@pytest.fixture
def sample_issue():
    """Sample issue data for testing."""
    return {
        "id": 1,
        "number": 42,
        "title": "Test Issue",
        "body": "This is a test issue",
        "state": "open",
        "user": {
            "login": "octocat",
        },
        "labels": [
            {"name": "bug", "color": "d73a4a"},
        ],
        "assignees": [],
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-05T00:00:00Z",
    }


@pytest.fixture
def sample_pr():
    """Sample pull request data for testing."""
    return {
        "id": 1,
        "number": 123,
        "title": "Test Pull Request",
        "body": "This is a test PR",
        "state": "open",
        "user": {
            "login": "octocat",
        },
        "head": {
            "ref": "feature-branch",
            "sha": "abc123",
        },
        "base": {
            "ref": "main",
            "sha": "def456",
        },
        "draft": False,
        "merged": False,
        "mergeable": True,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-05T00:00:00Z",
    }


@pytest.fixture
def mock_auth_token():
    """Mock authentication token for testing."""
    return "ghp_test_token_1234567890abcdefghijklmnopqrstuvwxyz"


@pytest.fixture
def mock_user():
    """Mock authenticated user for testing."""
    from src.api.middleware.auth import TokenData

    return TokenData(username="testuser", scopes=["repo", "read:org"])
