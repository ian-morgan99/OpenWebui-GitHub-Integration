"""Unit Tests for Validators"""
import pytest

from src.utils.validators import (
    validate_branch_name,
    validate_github_token,
    validate_repo_name,
    validate_semver,
)


class TestValidators:
    """Tests for validation functions."""

    def test_valid_repo_name(self):
        """Test validation of valid repository names."""
        assert validate_repo_name("Hello-World") is True
        assert validate_repo_name("my_repo") is True
        assert validate_repo_name("repo123") is True
        assert validate_repo_name("test.repo") is True

    def test_invalid_repo_name(self):
        """Test validation of invalid repository names."""
        assert validate_repo_name("") is False
        assert validate_repo_name(".dotstart") is False
        assert validate_repo_name("-dashstart") is False
        assert validate_repo_name("a" * 101) is False  # Too long

    def test_valid_branch_name(self):
        """Test validation of valid branch names."""
        assert validate_branch_name("main") is True
        assert validate_branch_name("feature/new-feature") is True
        assert validate_branch_name("bugfix/issue-123") is True
        assert validate_branch_name("release/v1.0.0") is True

    def test_invalid_branch_name(self):
        """Test validation of invalid branch names."""
        assert validate_branch_name("") is False
        assert validate_branch_name("/startslash") is False
        assert validate_branch_name("endslash/") is False
        assert validate_branch_name("double..dot") is False
        assert validate_branch_name("branch.lock") is False
        assert validate_branch_name("has space") is False
        assert validate_branch_name("has~tilde") is False

    def test_valid_github_token(self):
        """Test validation of valid GitHub tokens."""
        # Modern token format
        assert validate_github_token("ghp_" + "x" * 36) is True
        assert validate_github_token("gho_" + "x" * 36) is True
        # Legacy token format (40 hex chars)
        assert validate_github_token("a" * 40) is True

    def test_invalid_github_token(self):
        """Test validation of invalid GitHub tokens."""
        assert validate_github_token("") is False
        assert validate_github_token("invalid") is False
        assert validate_github_token("ghp_short") is False

    def test_valid_semver(self):
        """Test validation of valid semantic versions."""
        assert validate_semver("1.0.0") is True
        assert validate_semver("v1.0.0") is True
        assert validate_semver("0.1.0") is True
        assert validate_semver("1.0.0-alpha") is True
        assert validate_semver("1.0.0-beta.1") is True
        assert validate_semver("1.0.0+build.123") is True

    def test_invalid_semver(self):
        """Test validation of invalid semantic versions."""
        assert validate_semver("") is False
        assert validate_semver("1") is False
        assert validate_semver("1.0") is False
        assert validate_semver("v1.0") is False
        assert validate_semver("1.0.0.0") is False
