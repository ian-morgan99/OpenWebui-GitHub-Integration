"""Response Models for API Endpoints"""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class StandardResponse(BaseModel):
    """Standard API response wrapper."""

    success: bool = Field(..., description="Whether the operation was successful")
    message: str = Field(..., description="Human-readable message")
    data: Optional[Any] = Field(None, description="Response data")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "success": True,
                    "message": "Operation completed successfully",
                    "data": {"result": "example"},
                }
            ]
        }
    }


class ErrorResponse(BaseModel):
    """Error response model."""

    error: str = Field(..., description="Error type")
    detail: str = Field(..., description="Detailed error message")
    status_code: int = Field(..., description="HTTP status code")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "error": "ValidationError",
                    "detail": "Invalid input parameters",
                    "status_code": 400,
                }
            ]
        }
    }


class RepositoryHealthResponse(BaseModel):
    """Response model for repository health analysis."""

    health_score: float = Field(..., description="Overall health score (0-100)", ge=0, le=100)
    metrics: Dict[str, Any] = Field(..., description="Detailed health metrics")
    recommendations: List[str] = Field(..., description="List of recommendations for improvement")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "health_score": 85.5,
                    "metrics": {
                        "code_quality": 90,
                        "security": 80,
                        "documentation": 85,
                        "test_coverage": 75,
                        "ci_cd_status": 95,
                        "dependency_freshness": 70,
                        "community_health": 88,
                    },
                    "recommendations": [
                        "Improve test coverage (current: 75%, target: 80%)",
                        "Update outdated dependencies",
                        "Add security policy (SECURITY.md)",
                    ],
                }
            ]
        }
    }


class PaginatedResponse(BaseModel):
    """Paginated response wrapper."""

    items: List[Any] = Field(..., description="List of items")
    total: int = Field(..., description="Total number of items")
    page: int = Field(..., description="Current page number")
    per_page: int = Field(..., description="Items per page")
    total_pages: int = Field(..., description="Total number of pages")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "items": [{"id": 1}, {"id": 2}],
                    "total": 100,
                    "page": 1,
                    "per_page": 20,
                    "total_pages": 5,
                }
            ]
        }
    }
