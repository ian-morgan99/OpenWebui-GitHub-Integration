"""Mock GitHub API Responses for Testing"""


def mock_repository_response():
    """Mock GitHub repository API response."""
    return {
        "id": 1296269,
        "name": "Hello-World",
        "full_name": "octocat/Hello-World",
        "owner": {
            "login": "octocat",
            "id": 1,
            "type": "User",
        },
        "private": False,
        "description": "This is your first repo!",
        "fork": False,
        "created_at": "2011-01-26T19:01:12Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "pushed_at": "2024-01-01T00:00:00Z",
        "size": 180,
        "stargazers_count": 80,
        "watchers_count": 80,
        "language": "Python",
        "forks_count": 9,
        "open_issues_count": 0,
        "default_branch": "main",
    }


def mock_issue_response():
    """Mock GitHub issue API response."""
    return {
        "id": 1,
        "number": 1347,
        "title": "Found a bug",
        "user": {
            "login": "octocat",
            "id": 1,
        },
        "labels": [
            {
                "id": 208045946,
                "name": "bug",
                "description": "Something isn't working",
                "color": "d73a4a",
            }
        ],
        "state": "open",
        "assignee": None,
        "assignees": [],
        "milestone": None,
        "comments": 0,
        "created_at": "2011-04-22T13:33:48Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "closed_at": None,
        "body": "I'm having a problem with this.",
    }


def mock_pr_response():
    """Mock GitHub pull request API response."""
    return {
        "id": 1,
        "number": 1,
        "state": "open",
        "title": "Amazing new feature",
        "user": {
            "login": "octocat",
            "id": 1,
        },
        "body": "Please pull these awesome changes",
        "created_at": "2011-01-26T19:01:12Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "closed_at": None,
        "merged_at": None,
        "head": {
            "label": "octocat:new-topic",
            "ref": "new-topic",
            "sha": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
        },
        "base": {
            "label": "octocat:main",
            "ref": "main",
            "sha": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
        },
        "draft": False,
        "merged": False,
        "mergeable": True,
        "mergeable_state": "clean",
        "comments": 0,
        "commits": 1,
        "additions": 100,
        "deletions": 3,
        "changed_files": 5,
    }


def mock_release_response():
    """Mock GitHub release API response."""
    return {
        "id": 1,
        "tag_name": "v1.0.0",
        "target_commitish": "main",
        "name": "v1.0.0",
        "body": "## What's Changed\n\n- New feature\n- Bug fixes",
        "draft": False,
        "prerelease": False,
        "created_at": "2013-02-27T19:35:32Z",
        "published_at": "2013-02-27T19:35:32Z",
        "assets": [],
    }


def mock_rate_limit_response():
    """Mock GitHub rate limit API response."""
    return {
        "resources": {
            "core": {
                "limit": 5000,
                "remaining": 4999,
                "reset": 1372700873,
                "used": 1,
            },
            "search": {
                "limit": 30,
                "remaining": 18,
                "reset": 1372697452,
                "used": 12,
            },
            "graphql": {
                "limit": 5000,
                "remaining": 4993,
                "reset": 1372700389,
                "used": 7,
            },
        },
        "rate": {
            "limit": 5000,
            "remaining": 4999,
            "reset": 1372700873,
            "used": 1,
        },
    }
