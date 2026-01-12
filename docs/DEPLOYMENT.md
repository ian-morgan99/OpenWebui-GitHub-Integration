# Deployment Guide

## Local Development

### Prerequisites
- Python 3.11+
- PostgreSQL 16+ (optional)
- Redis 7+ (optional)

### Setup
```bash
./scripts/setup_dev.sh
source venv/bin/activate
cp .env.example .env
# Edit .env with your credentials
uvicorn src.main:app --reload
```

## Docker Deployment

### Using Docker Compose

```bash
cd deployment/docker
docker-compose up -d
```

Services started:
- Application (port 8000)
- PostgreSQL (port 5432)
- Redis (port 6379)
- Prometheus (port 9090)
- Grafana (port 3000)

### Using Docker

```bash
docker build -f deployment/docker/Dockerfile -t github-architect:latest .
docker run -p 8000:8000 --env-file .env github-architect:latest
```

## Kubernetes Deployment

### Prerequisites
- Kubernetes cluster
- kubectl configured
- Secrets configured

### Deployment Steps

1. **Create namespace**
```bash
kubectl create namespace github-architect
```

2. **Configure secrets**
```bash
kubectl apply -f deployment/kubernetes/secrets.yaml
```

3. **Apply ConfigMap**
```bash
kubectl apply -f deployment/kubernetes/configmap.yaml
```

4. **Deploy application**
```bash
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml
kubectl apply -f deployment/kubernetes/ingress.yaml
```

5. **Verify deployment**
```bash
kubectl get pods -n github-architect
kubectl get services -n github-architect
```

## Environment Variables

Required:
- `GITHUB_CLIENT_ID`
- `GITHUB_CLIENT_SECRET`
- `SECRET_KEY`
- `ENCRYPTION_KEY`

Optional:
- `DATABASE_URL`
- `REDIS_URL`
- `LOG_LEVEL`

See `.env.example` for complete list.

## Monitoring

### Prometheus
Access at: http://localhost:9090

### Grafana
Access at: http://localhost:3000
- Default credentials: admin/admin
- Configure Prometheus datasource
- Import dashboards from deployment/grafana/

## Health Checks

- Health: `/health`
- Readiness: `/health/ready`
- Metrics: `/metrics`

## Troubleshooting

### Application won't start
- Check environment variables
- Verify PostgreSQL/Redis connections
- Check logs: `docker logs <container>`

### Database connection issues
- Verify DATABASE_URL
- Check PostgreSQL is running
- Verify network connectivity

### Redis connection issues
- Verify REDIS_URL
- Check Redis is running
- Test with: `redis-cli ping`

## Production Checklist

- [ ] Secrets configured
- [ ] HTTPS/TLS enabled
- [ ] Database backups configured
- [ ] Monitoring setup
- [ ] Logging configured
- [ ] Rate limiting enabled
- [ ] Health checks passing
- [ ] Security scan passed
