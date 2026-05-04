# Event Booking DevOps Setup - Local Development Guide

## Quick Start on Your PC

### Option 1: Run with Docker Compose (Recommended)
```bash
docker-compose up --build
```
Then open: http://localhost:8501

### Option 2: Run with Docker directly
```bash
# Build the image
docker build -t event-booking:local .

# Run the container
docker run -p 8501:8501 -v %cd%/app:/app/app event-booking:local
```
Then open: http://localhost:8501

### Option 3: Run Streamlit directly (no Docker)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/main.py
```

## Docker Hub Configuration

Your Docker Hub username: **vitrag00**

When pushing images:
```bash
docker tag event-booking:local vitrag00/event-booking:latest
docker push vitrag00/event-booking:latest
```

## File Structure

- `Dockerfile` - Production-ready image (optimized)
- `Dockerfile.build` - Build-specific image (with dev dependencies)
- `docker-compose.yml` - Local development setup
- `Jenkinsfile` - CI/CD pipeline (uses your Docker Hub username)
- `k8s/` - Kubernetes manifests (for production deployment)
- `app/` - Streamlit application

## Stopping the Container

If running with docker-compose:
```bash
docker-compose down
```

If running with docker run:
```bash
docker stop event-booking-app
```

## Notes

- The app runs on port **8501** (Streamlit default)
- All configuration is set to work on localhost for local development
- Volume mounting ensures live code updates during development
