"""Integration Tests for API Endpoints"""
from fastapi import status


class TestAPIEndpoints:
    """Integration tests for API endpoints."""

    def test_health_endpoint(self, test_client):
        """Test health check endpoint."""
        response = test_client.get("/health")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"
        assert data["version"] == "0.1.0"

    def test_readiness_endpoint(self, test_client):
        """Test readiness check endpoint."""
        response = test_client.get("/health/ready")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "ready"
        assert "checks" in data

    def test_root_endpoint(self, test_client):
        """Test root endpoint."""
        response = test_client.get("/")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert data["version"] == "0.1.0"

    def test_metrics_endpoint(self, test_client):
        """Test Prometheus metrics endpoint."""
        response = test_client.get("/metrics")
        assert response.status_code == status.HTTP_200_OK
        # Metrics are in Prometheus text format
        assert "# HELP" in response.text or "# TYPE" in response.text or len(response.text) == 0

    def test_openapi_docs(self, test_client):
        """Test OpenAPI documentation is accessible."""
        response = test_client.get("/docs")
        assert response.status_code == status.HTTP_200_OK

    def test_openapi_json(self, test_client):
        """Test OpenAPI JSON is accessible."""
        response = test_client.get("/openapi.json")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "openapi" in data
        assert "info" in data

    # TODO: Add authentication tests
    # def test_authentication_required(self, test_client):
    #     """Test that protected endpoints require authentication."""
    #     response = test_client.post("/api/v1/repositories/analyze", json={})
    #     assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # TODO: Add rate limiting tests
    # def test_rate_limiting(self, test_client):
    #     """Test rate limiting functionality."""
    #     pass
