"""Error Handler Middleware"""
from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError


class NotFoundError(HTTPException):
    """Resource not found exception."""

    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class AuthenticationError(HTTPException):
    """Authentication failed exception."""

    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class RateLimitError(HTTPException):
    """Rate limit exceeded exception."""

    def __init__(self, detail: str = "Rate limit exceeded", retry_after: int = 60):
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=detail,
            headers={"Retry-After": str(retry_after)},
        )


class GitHubAPIError(HTTPException):
    """GitHub API error exception."""

    def __init__(self, detail: str, status_code: int = status.HTTP_502_BAD_GATEWAY):
        super().__init__(status_code=status_code, detail=f"GitHub API error: {detail}")


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handle HTTP exceptions and return standardized error response.
    
    Args:
        request: The request that caused the exception
        exc: The HTTP exception
        
    Returns:
        JSON response with error details
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.__class__.__name__,
            "detail": exc.detail,
            "status_code": exc.status_code,
        },
        headers=getattr(exc, "headers", None),
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    Handle validation exceptions and return detailed error information.
    
    Args:
        request: The request that caused the exception
        exc: The validation exception
        
    Returns:
        JSON response with validation error details
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "ValidationError",
            "detail": "Invalid input parameters",
            "status_code": 422,
            "errors": exc.errors(),
        },
    )


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Handle all other exceptions.
    
    Args:
        request: The request that caused the exception
        exc: The exception
        
    Returns:
        JSON response with generic error message
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "InternalServerError",
            "detail": "An unexpected error occurred. Please try again later.",
            "status_code": 500,
        },
    )
