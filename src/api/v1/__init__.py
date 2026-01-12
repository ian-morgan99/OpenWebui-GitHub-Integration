"""API v1 Router Configuration"""
from fastapi import APIRouter

from src.api.v1 import (
    analytics,
    dependencies,
    governance,
    issues,
    pull_requests,
    releases,
    repositories,
    security,
    teams,
)

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(repositories.router, prefix="/repositories", tags=["repositories"])
api_router.include_router(issues.router, prefix="/issues", tags=["issues"])
api_router.include_router(pull_requests.router, prefix="/pull-requests", tags=["pull-requests"])
api_router.include_router(releases.router, prefix="/releases", tags=["releases"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
api_router.include_router(security.router, prefix="/security", tags=["security"])
api_router.include_router(dependencies.router, prefix="/dependencies", tags=["dependencies"])
api_router.include_router(teams.router, prefix="/teams", tags=["teams"])
api_router.include_router(governance.router, prefix="/governance", tags=["governance"])
