# Apache Superset Production Deployment with Docker

[![Apache License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Docker Pulls](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com)
[![Production Ready](https://img.shields.io/badge/Status-Production%20Ready-green.svg)]()
[![Superset Version](https://img.shields.io/badge/Superset-v5.0.1-brightgreen.svg)](https://superset.apache.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7-red.svg)](https://redis.io/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v2-blue.svg)](https://docs.docker.com/compose/)
[![Security](https://img.shields.io/badge/Security-Hardened-purple.svg)]()
[![Documentation](https://img.shields.io/badge/Documentation-Comprehensive-orange.svg)]()

###### tags: `superset` `docker` `production` `enterprise` `analytics` `dashboard` `postgresql` `redis` `security` `monitoring` `high-availability` `scalable` `data-visualization` `bi-tools` `apache`

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
├── docker-compose.yml        # Docker services configuration
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
- SSH key configured with GitHub (for cloning)
- Minimum System Requirements:
  - CPU: 4 cores
  - RAM: 8GB
  - Storage: 20GB
- Network access for container communication

## Quick Start

1. Clone the repository to /opt/:
   ```bash
   # Using HTTPS
   sudo git clone https://github.com/NoneAvobeAll/Superset-Production-Deployment-with-Docker-.git /opt/superset
   # OR using SSH
   sudo git clone git@github.com:NoneAvobeAll/Superset-Production-Deployment-with-Docker-.git /opt/superset
   
   cd /opt/superset/

2.  Generate a secure SECRET_KEY using:
   ```bash
   openssl rand -base64 42
   ```
   Create and configure superset_config.py:
   ```bash
   cp superset_config/superset_config.py.example superset_config/superset_config.py
   ```
   Edit the `superset_config.py` file to set custom configurations.

3. Start the services:
   ```bash
   docker compose up -d
   ```

4. Create an Admin User (Required):
   ```bash
   # Access the Superset container
   docker exec -it superset bash

   # Create an admin user inside the container
   superset fab create-admin \
      --username admin \
      --firstname Superset \
      --lastname Admin \
      --email admin@superset.com \
      --password your_secure_password
   ```

5. Access Superset:
   - Open http://localhost:8090 in your browser
   - Log in with:
     - Username: admin
     - Password: your_secure_password

### Docker Commands Reference

1. Container Management:
   ```bash
   # View running containers
   docker ps
   
   # View all containers (including stopped)
   docker ps -a
   
   # View container logs
   docker logs superset
   docker logs superset-db
   docker logs superset-redis
   
   # Follow logs in real-time
   docker logs -f superset
   
   # Restart individual services
   docker restart superset
   docker restart superset-db
   docker restart superset-redis
   
   # Stop all services
   docker compose down
   
   # Stop and remove volumes (caution: this will delete data)
   docker compose down -v
   ```

2. Resource Monitoring:
   ```bash
   # View container resource usage
   docker stats
   
   # View container processes
   docker top superset
   
   # Inspect container details
   docker inspect superset
   ```

3. Data Management:
   ```bash
   # Backup PostgreSQL database
   docker exec superset-db pg_dump -U superset > backup.sql
   
   # Copy files from container
   docker cp superset:/app/superset_home/superset.db ./backup/
   
   # View volume information
   docker volume ls
   ```

4. Container Access:
   ```bash
   # Access container shells
   docker exec -it superset bash
   docker exec -it superset-db bash
   docker exec -it superset-redis bash
   ```

5. Service Updates:
   ```bash
   # Pull latest images
   docker compose pull
   
   # Update and restart services
   docker compose up -d --force-recreate
   
   # View image details
   docker images
   ```



### Maintenance Commands

1. Check container status:
   ```bash
   docker compose ps
   ```

2. Restart services:
   ```bash
   docker compose restart
   ```

3. Stop all services:
   ```bash
   docker compose down
   ```

4. Update containers:
   ```bash
   docker compose pull
   docker compose up -d
   ```

### Accessing Container Shell
```bash
# List containers
docker ps

# Access Superset container
sudo docker exec -it CONTAINER_ID bash

# Common commands inside container 
superset db upgrade                  # Run database migrations
```

## Guest role permissions
- Read access to all charts and dashboards
- JSON exploration capabilities
- Data sampling
- Database access (read-only)

 execute guestRole.py inside container, paste the script inside container shell.

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