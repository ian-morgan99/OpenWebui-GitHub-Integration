# 🏗️ GitHub Architect Tool Server

**Production-ready GitHub operations server for OpenWebUI integration**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive GitHub operations server designed for solution architects, providing enterprise-grade GitHub repository management, analytics, and automation capabilities through a RESTful API.

## ✨ Features

### Repository Management
- 📊 **Repository Health Analysis** - Comprehensive health scoring and recommendations
- 📈 **Metrics & Analytics** - Commit frequency, contributor activity, PR/issue trends
- 🔍 **Multi-Repository Operations** - Bulk operations across multiple repositories
- 📋 **CODEOWNERS Analysis** - Analyze code ownership and coverage

### Issue & PR Management
- 🎫 **Issue Operations** - Create, update, list, and bulk-update issues
- 🔀 **Pull Request Workflow** - Complete PR lifecycle management
- 👀 **Code Reviews** - Submit reviews, approve, or request changes
- 🔗 **Automated PR Creation** - Create PRs from templates

### Release Management
- 🚀 **Release Planning** - AI-powered release planning with semantic versioning
- 📝 **Changelog Generation** - Automatic changelog creation from commits
- 🏷️ **Release Automation** - Create and publish releases with assets

### Analytics & Insights
- 📊 **Team Metrics** - Team velocity, workload distribution, collaboration patterns
- 🎯 **Bottleneck Detection** - Identify development bottlenecks
- 📉 **PR Review Analytics** - Review distribution and patterns
- 🔥 **Code Churn Analysis** - Track code stability and change frequency

### Security & Compliance
- 🔒 **Security Scanning** - Vulnerability detection and analysis
- 📋 **Compliance Reports** - SOC2, GDPR compliance checking
- 🛡️ **Branch Protection Audit** - Verify branch protection settings
- 🔐 **Secret Scanning** - Detect exposed secrets

### Dependency Management
- 📦 **Dependency Analysis** - Analyze and visualize dependency trees
- ⚠️ **Vulnerability Detection** - Scan for known vulnerabilities
- 🔄 **Update Recommendations** - Suggest dependency updates
- 📄 **License Compliance** - Check license compatibility

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- GitHub OAuth App credentials ([Create one](https://github.com/settings/applications/new))
- PostgreSQL 16+ (optional, for audit logs)
- Redis 7+ (optional, for caching)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ian-morgan99/OpenWebui-GitHub-Integration.git
cd OpenWebui-GitHub-Integration
```

2. **Run the setup script**
```bash
./scripts/setup_dev.sh
source venv/bin/activate
```

3. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your GitHub OAuth credentials and secrets
```

4. **Generate secret keys**
```bash
openssl rand -hex 32  # For SECRET_KEY
openssl rand -hex 32  # For ENCRYPTION_KEY
```

5. **Start the server**
```bash
uvicorn src.main:app --reload
```

6. **Access the API**
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- API Endpoints: http://localhost:8000/api/v1/

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
cd deployment/docker
docker-compose up -d
```

This starts:
- 🚀 FastAPI application (port 8000)
- 🗄️ PostgreSQL database (port 5432)
- 📊 Redis cache (port 6379)
- 📈 Prometheus metrics (port 9090)
- 📊 Grafana dashboards (port 3000)

### Using Docker

```bash
docker build -f deployment/docker/Dockerfile -t github-architect:latest .
docker run -p 8000:8000 --env-file .env github-architect:latest
```

## ☸️ Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f deployment/kubernetes/

# Check deployment status
kubectl get pods
kubectl get services
```

## 📖 Documentation

- [Architecture](docs/ARCHITECTURE.md) - System design and architecture
- [API Documentation](docs/API.md) - Complete API reference
- [Security](docs/SECURITY.md) - Security best practices
- [Deployment Guide](docs/DEPLOYMENT.md) - Deployment instructions
- [Contributing](docs/CONTRIBUTING.md) - How to contribute

## 🔧 Configuration

Key environment variables:

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GITHUB_CLIENT_ID` | GitHub OAuth App Client ID | Yes | - |
| `GITHUB_CLIENT_SECRET` | GitHub OAuth App Secret | Yes | - |
| `SECRET_KEY` | JWT signing key | Yes | - |
| `ENCRYPTION_KEY` | Token encryption key | Yes | - |
| `DATABASE_URL` | PostgreSQL connection URL | No | `postgresql://...` |
| `REDIS_URL` | Redis connection URL | No | `redis://localhost:6379/0` |
| `LOG_LEVEL` | Logging level | No | `INFO` |

See [.env.example](.env.example) for complete configuration options.

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_validators.py

# Run integration tests only
pytest tests/integration/
```

## 📊 API Examples

### Analyze Repository Health

```bash
curl -X POST "http://localhost:8000/api/v1/repositories/analyze" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "repo_owner": "octocat",
    "repo_name": "Hello-World",
    "token": "ghp_xxxxxxxxxxxx"
  }'
```

### Create an Issue

```bash
curl -X POST "http://localhost:8000/api/v1/issues/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "repo_owner": "octocat",
    "repo_name": "Hello-World",
    "title": "Bug: Application crashes",
    "body": "Description of the bug...",
    "labels": ["bug", "critical"],
    "token": "ghp_xxxxxxxxxxxx"
  }'
```

### Get Team Metrics

```bash
curl -X POST "http://localhost:8000/api/v1/analytics/team-metrics" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "org": "your-org",
    "team": "engineering",
    "time_window_days": 30,
    "token": "ghp_xxxxxxxxxxxx"
  }'
```

## 🤝 OpenWebUI Integration

This server is designed to work seamlessly with OpenWebUI. Example queries:

```
"Analyze the health of octocat/Hello-World repository"
"Create an issue in my-repo about the login bug"
"Show me team velocity metrics for the last sprint"
"Generate a release plan for v2.0.0"
```

## 🛠️ Development

### Project Structure

```
.
├── src/
│   ├── api/          # API endpoints and middleware
│   ├── core/         # Core business logic
│   ├── models/       # Pydantic models
│   ├── services/     # External service integrations
│   └── utils/        # Utility functions
├── tests/            # Test suite
├── deployment/       # Docker and Kubernetes configs
├── docs/             # Documentation
└── scripts/          # Utility scripts
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/

# Type checking
mypy src/

# Security scan
bandit -r src/

# Run pre-commit hooks
pre-commit run --all-files
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- GitHub API integration via [PyGithub](https://github.com/PyGithub/PyGithub)
- Designed for [OpenWebUI](https://github.com/open-webui/open-webui)

## 📞 Support

- 📧 Email: team@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/ian-morgan99/OpenWebui-GitHub-Integration/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/ian-morgan99/OpenWebui-GitHub-Integration/discussions)

## 🗺️ Roadmap

- [x] Core API endpoints
- [x] GitHub OAuth integration
- [x] Repository health analysis
- [ ] Advanced analytics dashboard
- [ ] Webhook support
- [ ] GraphQL API support
- [ ] Multi-org management
- [ ] Custom integrations

---

**Made with ❤️ for Solution Architects**
