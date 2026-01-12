"""Authentication and Authorization Middleware"""
from typing import Optional

from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2AuthorizationCodeBearer

from src.config.settings import settings

# OAuth2 scheme for OpenAPI documentation
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://github.com/login/oauth/authorize",
    tokenUrl="/auth/token",
    scopes={
        "repo": "Full control of private repositories",
        "read:org": "Read org and team membership",
        "user:email": "Access user email addresses",
    },
)

# HTTP Bearer scheme for token authentication
security = HTTPBearer()


class TokenData:
    """Data extracted from JWT token."""

    def __init__(self, username: Optional[str] = None, scopes: Optional[list] = None):
        self.username = username
        self.scopes = scopes or []


async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)) -> TokenData:
    """
    Dependency to get the current authenticated user from JWT token.
    
    Args:
        credentials: HTTP authorization credentials
        
    Returns:
        TokenData with user information
        
    Raises:
        HTTPException: If token is invalid or missing
    """
    # Check if authentication bypass is enabled
    if settings.BYPASS_AUTHENTICATION:
        # Return dummy user for development only - NOT FOR PRODUCTION
        return TokenData(username="dev-user", scopes=["repo"])
    
    # TODO: Implement actual JWT validation
    # This is a skeleton implementation
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token = credentials.credentials
    
    if not token:
        raise credentials_exception
    
    # TODO: Implement JWT validation
    # try:
    #     payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    #     username: str = payload.get("sub")
    #     if username is None:
    #         raise credentials_exception
    #     token_scopes = payload.get("scopes", [])
    # except JWTError:
    #     raise credentials_exception
    
    # Skeleton: return dummy user until JWT validation is implemented
    return TokenData(username="user", scopes=["repo"])


async def validate_token(token: str) -> bool:
    """
    Validate a JWT token.
    
    Args:
        token: JWT token to validate
        
    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement JWT token validation
    # try:
    #     jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    #     return True
    # except JWTError:
    #     return False
    return True


async def validate_scopes(required_scopes: list, token_scopes: list) -> bool:
    """
    Validate that token has required scopes.
    
    Args:
        required_scopes: List of required scope names
        token_scopes: List of scopes in the token
        
    Returns:
        True if token has all required scopes, False otherwise
    """
    return all(scope in token_scopes for scope in required_scopes)


# OAuth 2.0 Flow Implementation
# TODO: Implement the following endpoints in a separate auth router:
# 
# @router.get("/auth/github")
# async def github_oauth_login():
#     """Redirect to GitHub OAuth authorization page."""
#     pass
#
# @router.get("/auth/callback")
# async def github_oauth_callback(code: str):
#     """Handle GitHub OAuth callback and exchange code for token."""
#     pass
#
# @router.post("/auth/token")
# async def refresh_token():
#     """Refresh an expired access token."""
#     pass
#
# @router.post("/auth/revoke")
# async def revoke_token():
#     """Revoke an access token."""
#     pass
