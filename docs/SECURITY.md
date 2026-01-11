# Security

## Authentication

### OAuth 2.0 Flow

1. User initiates OAuth flow
2. Redirected to GitHub authorization
3. GitHub callback with authorization code
4. Server exchanges code for access token
5. Token encrypted and stored
6. JWT token issued to client

### JWT Tokens

- **Algorithm**: RS256
- **Expiration**: 30 minutes
- **Refresh**: Available via refresh endpoint

## Authorization

All API requests require valid JWT token in Authorization header.

## Token Storage

- Access tokens encrypted at rest
- Encryption key required in environment
- Tokens stored securely in database

## Rate Limiting

- Per-user rate limits enforced
- Redis-based rate limiting
- Configurable limits per endpoint

## Security Best Practices

### Secrets Management

- Never commit secrets to version control
- Use environment variables
- Rotate keys regularly
- Use secrets management systems (AWS Secrets Manager, Vault, etc.)

### Input Validation

- All inputs validated with Pydantic
- SQL injection prevention
- XSS prevention
- CSRF protection

### HTTPS/TLS

- Always use HTTPS in production
- TLS 1.2 or higher
- Strong cipher suites

## Vulnerability Reporting

Please report security vulnerabilities to: security@example.com

**Do not** create public issues for security vulnerabilities.

## Security Headers

- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- X-XSS-Protection: 1; mode=block
- Strict-Transport-Security: max-age=31536000

## Compliance

- GDPR compliant
- SOC2 compatible
- Regular security audits
