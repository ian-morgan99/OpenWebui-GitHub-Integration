"""Prometheus Metrics Configuration"""
from prometheus_client import Counter, Gauge, Histogram

# API Request metrics
request_counter = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status_code']
)

request_duration = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

# GitHub API metrics
github_api_requests = Counter(
    'github_api_requests_total',
    'Total GitHub API requests',
    ['operation', 'status']
)

github_api_rate_limit = Gauge(
    'github_api_rate_limit_remaining',
    'Remaining GitHub API rate limit',
    ['token_type']
)

# Cache metrics
cache_hits = Counter(
    'cache_hits_total',
    'Total cache hits',
    ['cache_type']
)

cache_misses = Counter(
    'cache_misses_total',
    'Total cache misses',
    ['cache_type']
)

# Error metrics
error_counter = Counter(
    'errors_total',
    'Total errors',
    ['error_type', 'endpoint']
)

# Business metrics
repository_analyses = Counter(
    'repository_analyses_total',
    'Total repository analyses performed',
    ['status']
)

issues_created = Counter(
    'issues_created_total',
    'Total issues created',
    ['repo_owner']
)

pull_requests_created = Counter(
    'pull_requests_created_total',
    'Total pull requests created',
    ['repo_owner']
)

# System metrics
active_connections = Gauge(
    'active_connections',
    'Number of active connections',
    ['connection_type']
)
