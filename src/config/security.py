"""Security Configuration and Settings"""
from typing import List


class SecurityConfig:
    """Security configuration for the application."""

    # Password Hashing
    PWD_CONTEXT_SCHEMES: List[str] = ["bcrypt"]
    PWD_CONTEXT_DEPRECATED: str = "auto"

    # CORS Settings
    CORS_MAX_AGE: int = 600  # 10 minutes

    # Allowed Hosts (for production)
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "*.github-architect.com"]

    # Security Headers
    SECURITY_HEADERS = {
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
        "X-XSS-Protection": "1; mode=block",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Content-Security-Policy": "default-src 'self'",
    }

    # Token Settings
    TOKEN_TYPE: str = "Bearer"
    TOKEN_URL: str = "/auth/token"

    # OAuth Scopes Required
    REQUIRED_GITHUB_SCOPES: List[str] = [
        "repo",  # Full control of private repositories
        "read:org",  # Read org and team membership
        "user:email",  # Access user email addresses
    ]


# Global security config instance
security_config = SecurityConfig()
