"""Application Settings and Configuration Management"""
from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True)

    # Application
    APP_NAME: str = "GitHub Architect Tool Server"
    APP_DESCRIPTION: str = "Production-ready GitHub operations server for OpenWebUI integration"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = Field(default="development", description="Environment: development, staging, production")
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")

    # GitHub OAuth
    GITHUB_CLIENT_ID: str = Field(default="", description="GitHub OAuth App Client ID")
    GITHUB_CLIENT_SECRET: str = Field(default="", description="GitHub OAuth App Client Secret")
    GITHUB_CALLBACK_URL: str = Field(
        default="http://localhost:8000/auth/callback", description="OAuth callback URL"
    )

    # Security
    SECRET_KEY: str = Field(default="", description="Secret key for JWT signing (generate with openssl rand -hex 32)")
    ENCRYPTION_KEY: str = Field(
        default="", description="Encryption key for token storage (generate with openssl rand -hex 32)"
    )
    ALGORITHM: str = Field(default="RS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Access token expiration time in minutes")

    # Database
    DATABASE_URL: str = Field(
        default="postgresql://postgres:password@localhost:5432/github_architect",
        description="PostgreSQL connection URL",
    )

    # Redis
    REDIS_URL: str = Field(default="redis://localhost:6379/0", description="Redis connection URL")

    # Rate Limiting
    DEFAULT_RATE_LIMIT: str = Field(default="1000/hour", description="Default rate limit per user")

    # CORS
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8080"],
        description="Allowed CORS origins",
    )
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, v: str) -> str:
        """Validate that SECRET_KEY is set in production."""
        if not v:
            raise ValueError("SECRET_KEY must be set")
        if len(v) < 32:
            raise ValueError("SECRET_KEY must be at least 32 characters long")
        return v

    @field_validator("ENCRYPTION_KEY")
    @classmethod
    def validate_encryption_key(cls, v: str) -> str:
        """Validate that ENCRYPTION_KEY is set."""
        if not v:
            raise ValueError("ENCRYPTION_KEY must be set")
        if len(v) < 32:
            raise ValueError("ENCRYPTION_KEY must be at least 32 characters long")
        return v


# Global settings instance
settings = Settings()
