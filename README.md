# Apache Superset Production Deployment with Docker

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Docker Pulls](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com)
[![Production Ready](https://img.shields.io/badge/Status-Production%20Ready-green.svg)]()

A production-hardened Docker Compose setup for Apache Superset with enterprise-grade configurations, including PostgreSQL as the metadata database and Redis for caching and async task management.

## Author
**Abubakkar Khan**  
*System Admin*

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Security](#security)
- [Monitoring](#monitoring)
- [Maintenance](#maintenance)
- [Backup & Recovery](#backup--recovery)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

### Project Structure
```
.
├── docker-compose.yml
├── .env.example              # Template for environment variables
├── README.md
├── superset_config
│   └── superset_config.py    # Custom Superset configurations
└── superset_custom
    └── Dockerfile            # Custom Docker build instructions
```

### Components
- **Superset**: Custom build v5.0.1
  - Production-optimized configurations
  - Enhanced security features
  - Custom timezone settings
- **PostgreSQL**: v15 (Metadata Store)
  - Optimized for production workloads
  - Persistent storage
- **Redis**: v7
  - Session management
  - Caching layer
  - Async task queue

### Features
- ✅ Production-grade security configurations
- ✅ Container health monitoring
- ✅ Automated database migrations
- ✅ Log rotation
- ✅ Volume persistence
- ✅ Non-root user execution
- ✅ Resource management
- ✅ High availability ready

## Architecture
```
┌─────────────────┐     ┌─────────────────┐
│    Superset     │────▶│     Redis       │
│   (Web + API)   │     │  (Cache/Queue)  │
└────────┬────────┘     └─────────────────┘
         │
         │
         ▼
┌─────────────────┐
│   PostgreSQL    │
│  (Metadata DB)  │
└─────────────────┘
```

## Prerequisites
- Docker Engine 24.x or later
- Docker Compose v2.x or later
- Minimum System Requirements:
  - CPU: 4 cores
  - RAM: 8GB
  - Storage: 20GB
- Network access for container communication

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/superset-docker.git
   cd superset-docker
   ```

2. Create and configure environment file:
   ```bash
   cp .env.example .env
   ```
   The .env file requires three secure values:
   ```env
   POSTGRES_PASSWORD=<your-secure-postgres-password>
   REDIS_PASSWORD=<your-secure-redis-password>
   SECRET_KEY=<your-generated-secret-key>
   ```
   Generate a secure SECRET_KEY using:
   ```bash
   openssl rand -base64 42
   ```

3. Start the services:
   ```bash
   docker-compose up -d
   ```
   The docker-compose file will automatically:
   - Upgrade the database (`superset db upgrade`)
   - Initialize Superset (`superset init`)
   - Start the application

4. Create an Admin User:
   ```bash
   # Get the Superset container ID or use container name
   docker exec -it superset bash

   # Create an admin user inside the container
   superset fab create-admin \
      --username admin \
      --firstname Superset \
      --lastname Admin \
      --email admin@superset.com \
      --password your_secure_password
   ```

   Note: This is the only manual step required after deployment.

6. Access Superset at http://localhost:8090 and log in with:
   - Username: admin
   - Password: your_secure_password

## Running the Project

### First Time Setup
1. Ensure Docker and Docker Compose are installed:
   ```bash
   docker --version
   docker-compose --version
   ```

2. Clone and navigate to the project:
   ```bash
   git clone https://github.com/your-repo/superset-docker.git
   cd superset-docker
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your preferred text editor
   nano .env
   ```

4. Start the application:
   ```bash
   docker-compose up -d
   ```

5. Monitor the startup:
   ```bash
   docker-compose logs -f
   ```

### Maintenance Commands

1. Check container status:
   ```bash
   docker-compose ps
   ```

2. Restart services:
   ```bash
   docker-compose restart
   ```

3. Stop all services:
   ```bash
   docker-compose down
   ```

4. Update containers:
   ```bash
   docker-compose pull
   docker-compose up -d
   ```

### Accessing Container Shell
```bash
# List containers
docker ps

# Access Superset container
sudo docker exec -it CONTAINER_ID bash

# Common commands inside container
superset db upgrade                  # Run database migrations
superset init                       # Initialize Superset
superset fab create-admin          # Create another admin user
superset load_examples             # Load example dashboards
```

## Configuration

### Environment Variables
Detailed list of configurable environment variables:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| POSTGRES_DB | Database name | superset | Yes |
| POSTGRES_USER | Database user | superset | Yes |
| POSTGRES_PASSWORD | Database password | - | Yes |
| SUPERSET_ENV | Environment type | production | Yes |
| REDIS_HOST | Redis hostname | redis | Yes |

### Custom Configurations
- Timezone: Asia/Dhaka
- Cache timeout: 300 seconds
- SQL Lab timeout: 600 seconds
- Maximum log file size: 50MB
- Log retention: 5 files

## Security
- Non-root container execution
- Dropped container capabilities
- No privilege escalation
- Regular security updates
- TLS/SSL support
- Authentication required
- Rate limiting enabled

## Monitoring
### Health Checks
- **Superset**: `/health` endpoint (1-minute intervals)
- **PostgreSQL**: Database connectivity (30-second intervals)
- **Redis**: Server ping (30-second intervals)

### Logging
All services use JSON logging with rotation:
```yaml
logging:
  driver: "json-file"
  options:
    max-size: "50m"
    max-file: "5"
```

## Maintenance

### Regular Tasks
1. Database backup (daily)
2. Log rotation (automated)
3. Security updates (weekly)
4. Performance monitoring
5. Storage cleanup

### Scaling Guidelines
- Horizontal scaling via Docker Swarm/Kubernetes
- Vertical scaling recommendations
- Cache optimization strategies

## Backup & Recovery

### Backup Strategy
1. Database Dumps:
   ```bash
   docker exec superset-db pg_dump -U superset > backup.sql
   ```

2. Volume Backups:
   - superset_home
   - superset_db_data
   - redis_data

### Recovery Procedures
Detailed recovery steps for various failure scenarios

## Troubleshooting

### Common Issues
1. Container startup failures
2. Database connection issues
3. Redis connectivity problems
4. Permission errors

### Debug Tools
- Container logs
- Health check status
- Resource monitoring
- Network diagnostics

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Create Pull Request

## License
Apache License 2.0 - See LICENSE file for details

---
Last updated: September 24, 2025  
Maintained by: Abubakkar Khan (System Admin)