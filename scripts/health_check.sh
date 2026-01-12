#!/bin/bash
# Health check script for deployment verification

ENDPOINT=${1:-http://localhost:8000}
MAX_RETRIES=5
RETRY_DELAY=2

echo "Checking health of $ENDPOINT"

for i in $(seq 1 $MAX_RETRIES); do
    echo "Attempt $i/$MAX_RETRIES..."
    
    if curl -f -s "$ENDPOINT/health" > /dev/null; then
        echo "✓ Health check passed"
        exit 0
    fi
    
    if [ $i -lt $MAX_RETRIES ]; then
        echo "  Health check failed, retrying in ${RETRY_DELAY}s..."
        sleep $RETRY_DELAY
    fi
done

echo "✗ Health check failed after $MAX_RETRIES attempts"
exit 1
