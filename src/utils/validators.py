"""Validation Utilities"""
import re


def validate_repo_name(name: str) -> bool:
    """
    Validate a GitHub repository name.
    
    Args:
        name: Repository name to validate
        
    Returns:
        True if valid, False otherwise
        
    Rules:
        - Can contain alphanumeric characters, hyphens, underscores, and periods
        - Cannot start with a period or hyphen
        - Must be 1-100 characters long
    """
    if not name or len(name) > 100:
        return False
    
    pattern = r'^[a-zA-Z0-9_][a-zA-Z0-9._-]*$'
    return bool(re.match(pattern, name))


def validate_branch_name(name: str) -> bool:
    """
    Validate a Git branch name.
    
    Args:
        name: Branch name to validate
        
    Returns:
        True if valid, False otherwise
        
    Rules:
        - Cannot start or end with a slash
        - Cannot contain two consecutive dots (..)
        - Cannot contain special characters: ~, ^, :, ?, *, [, \\, space, ASCII control characters
        - Cannot end with .lock
    """
    if not name or len(name) > 255:
        return False
    
    # Check forbidden patterns
    if name.startswith('/') or name.endswith('/'):
        return False
    if '..' in name:
        return False
    if name.endswith('.lock'):
        return False
    
    # Check for forbidden characters
    forbidden_chars = ['~', '^', ':', '?', '*', '[', '\\', ' ']
    if any(char in name for char in forbidden_chars):
        return False
    
    # Check for ASCII control characters
    if any(ord(char) < 32 or ord(char) == 127 for char in name):
        return False
    
    return True


def validate_github_token(token: str) -> bool:
    """
    Validate a GitHub personal access token format.
    
    Args:
        token: GitHub token to validate
        
    Returns:
        True if format is valid, False otherwise
        
    Note:
        This only validates the format, not whether the token is active or has correct permissions.
    """
    if not token:
        return False
    
    # GitHub tokens typically start with specific prefixes:
    # - ghp_ for personal access tokens
    # - gho_ for OAuth tokens
    # - ghu_ for user-to-server tokens
    # - ghs_ for server-to-server tokens
    # - ghr_ for refresh tokens
    valid_prefixes = ['ghp_', 'gho_', 'ghu_', 'ghs_', 'ghr_']
    
    if any(token.startswith(prefix) for prefix in valid_prefixes):
        # Modern GitHub token format
        return len(token) >= 40
    
    # Legacy tokens (40 character hex string)
    if len(token) == 40 and re.match(r'^[a-f0-9]{40}$', token):
        return True
    
    return False


def validate_semver(version: str) -> bool:
    """
    Validate semantic versioning format.
    
    Args:
        version: Version string to validate (e.g., "1.0.0", "v2.1.3")
        
    Returns:
        True if valid semver, False otherwise
    """
    # Remove optional 'v' prefix
    version = version.lstrip('v')
    
    pattern = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'
    return bool(re.match(pattern, version))
