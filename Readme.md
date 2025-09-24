# Apache Superset Production Deployment with Docker 

This repository contains a production-ready Docker Compose setup for Apache Superset with custom configurations, including PostgreSQL as the metadata database and Redis for caching.

## Components

- **Superset**: Custom build based on version 5.0.1
- **PostgreSQL**: Version 15 for metadata storage
- **Redis**: Version 7 for caching and async tasks

## Prerequisites

- Docker and Docker Compose
- At least 4GB of RAM
- Sufficient disk space for data persistence

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# PostgreSQL
POSTGRES_DB=superset
POSTGRES_USER=superset
POSTGRES_PASSWORD=your_secure_password

# Superset
SUPERSET_ENV=production
DATABASE_URL=postgresql+psycopg2://superset:your_secure_password@db:5432/superset
REDIS_HOST=redis
```

### Custom Configuration

The setup includes customized configurations:

- Timezone set to Asia/Dhaka
- Redis caching enabled with 5-minute default timeout
- SQL Lab timeout set to 600 seconds
- Security features configured for production use
- Log rotation enabled (50MB max size, 5 files max)

## Ports

- Superset web interface: Port 8090 (Host) -> 8088 (Container)
- PostgreSQL: Internal access only
- Redis: Internal access only

## Volumes

The setup includes three persistent volumes:

- `superset_db_data`: PostgreSQL data
- `redis_data`: Redis data
- `superset_home`: Superset home directory

## Security Features

- Container runs as non-root user
- Dropped all capabilities by default
- No new privileges allowed
- Health checks configured for all services
- Log rotation enabled

## Usage

1. Clone this repository
2. Create the `.env` file with appropriate values
3. Start the services:
   ```bash
   docker-compose up -d
   ```
4. Access Superset at http://localhost:8090

## Health Checks

- **Superset**: Checks `/health` endpoint every minute
- **PostgreSQL**: Checks database connectivity every 30 seconds
- **Redis**: Pings Redis server every 30 seconds

## Maintenance

### Logs
All services use JSON file logging with rotation:
- Maximum file size: 50MB
- Maximum number of files: 5

### Backups
Remember to regularly backup:
- PostgreSQL data volume
- Superset home volume
- Redis data (if persistent caching is critical)

## Support

For issues and support, please contact the system administrator.

## License

Refer to the project's LICENSE file for licensing information.
