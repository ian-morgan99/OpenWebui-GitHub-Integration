"""GitHub Architect Tool Server - Main FastAPI Application"""
import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

from src.api.v1 import api_router
from src.config.settings import settings
from src.utils.logger import setup_logging
from src.utils.metrics import request_counter, request_duration

# Setup structured logging
setup_logging(settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """Handle application startup and shutdown events."""
    # Startup
    logger.info(
        "Starting GitHub Architect Tool Server",
        extra={
            "version": "0.1.0",
            "environment": settings.ENVIRONMENT,
            "app_name": settings.APP_NAME,
        },
    )
    yield
    # Shutdown
    logger.info("Shutting down GitHub Architect Tool Server")


# Initialize FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)


# Middleware for request tracking
@app.middleware("http")
async def track_requests(request: Request, call_next):
    """Track requests with Prometheus metrics."""
    response = await call_next(request)
    
    # Track after response to avoid errors breaking the request
    try:
        request_counter.labels(
            method=request.method,
            endpoint=request.url.path,
            status_code=response.status_code
        ).inc()
    except Exception:
        # Don't let metrics tracking break the response
        pass
    
    return response


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle all unhandled exceptions."""
    logger.error(
        "Unhandled exception",
        extra={
            "error": str(exc),
            "path": request.url.path,
            "method": request.method,
        },
        exc_info=True,
    )
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": "An unexpected error occurred. Please try again later.",
        },
    )


# Root endpoint
@app.get("/", tags=["root"])
async def root():
    """Root endpoint with welcome message and API information."""
    return {
        "message": "Welcome to GitHub Architect Tool Server",
        "version": "0.1.0",
        "docs": "/docs",
        "openapi": "/openapi.json",
        "health": "/health",
        "api": settings.API_V1_PREFIX,
    }


# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "version": "0.1.0",
    }


# Readiness check endpoint
@app.get("/health/ready", tags=["health"])
async def readiness_check():
    """Readiness check endpoint - checks if dependencies are available."""
    # TODO: Add actual dependency checks (Redis, PostgreSQL, GitHub API)
    checks = {
        "database": "unknown",  # TODO: Check PostgreSQL connection
        "cache": "unknown",  # TODO: Check Redis connection
        "github_api": "unknown",  # TODO: Check GitHub API reachability
    }
    
    return {
        "status": "ready",
        "version": "0.1.0",
        "checks": checks,
    }


# Prometheus metrics endpoint
@app.get("/metrics", tags=["metrics"])
async def metrics():
    """Prometheus metrics endpoint."""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


# Include API v1 router
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level=settings.LOG_LEVEL.lower(),
    )
