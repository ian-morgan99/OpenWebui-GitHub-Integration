# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All API requests require authentication using a Bearer token:

```bash
Authorization: Bearer YOUR_JWT_TOKEN
```

## Endpoints

### Health Check

**GET** `/health`

Returns server health status.

### Repositories

**POST** `/api/v1/repositories/analyze`

Analyze repository health and get recommendations.

**GET** `/api/v1/repositories/{owner}/{repo}/info`

Get detailed repository information.

**POST** `/api/v1/repositories/list`

List repositories with filters.

### Issues

**POST** `/api/v1/issues/create`

Create a new issue.

**POST** `/api/v1/issues/list`

List issues with filters.

**GET** `/api/v1/issues/{owner}/{repo}/{number}`

Get issue details.

### Pull Requests

**POST** `/api/v1/pull-requests/create`

Create a new pull request.

**POST** `/api/v1/pull-requests/{owner}/{repo}/{number}/review`

Submit a code review.

**POST** `/api/v1/pull-requests/{owner}/{repo}/{number}/merge`

Merge a pull request.

## Rate Limiting

Default rate limit: 1000 requests per hour per user.

Rate limit headers:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1234567890
```

## Error Codes

- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `429` - Too Many Requests
- `500` - Internal Server Error

## Complete Documentation

For complete API documentation, visit: http://localhost:8000/docs
