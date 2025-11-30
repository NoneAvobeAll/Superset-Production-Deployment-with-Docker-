# ------------------------------
# Alternative Superset Production Docker Image
# Author: Abubakkar, System Admin  
# Based on Apache Superset 4.0.2 (more stable with drivers)
# ------------------------------

FROM apache/superset:5.0.0

# Switch to root for installations
USER root

# Install essential system packages for DB drivers and utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      gcc \
      g++ \
      libpq-dev \
      default-libmysqlclient-dev \
      freetds-dev \
      pkg-config \
      curl \
      netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Install essential Python database drivers and production packages
RUN . /app/.venv/bin/activate && \
      uv pip install \
      psycopg2-binary \
      PyMySQL \
      mysqlclient \
      pymssql \
      openpyxl \
      redis \
      flask-cors \
      gunicorn \
      gevent

# Verify installations
RUN python -c "import psycopg2; print('psycopg2 OK')" && \
    python -c "import redis; print('redis OK')" && \
    python -c "import flask_cors; print('flask-cors OK')"

# Clean up build dependencies to reduce image size
RUN apt-get purge -y \
      build-essential \
      gcc \
      g++ \
      libpq-dev \
      pkg-config && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Switch back to superset user
USER superset

# Set working directory
WORKDIR /app

# Set environment for Superset
ENV FLASK_APP=superset
ENV PYTHONPATH="/app/pythonpath:$PYTHONPATH"

# Expose Superset port
EXPOSE 8088

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8088/health || exit 1

# Start Superset
CMD ["superset", "run", "-h", "0.0.0.0", "-p", "8088"]

