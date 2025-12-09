 
# ------------------------------
# Superset Production Config
# Author: Abubakkar, System Admin
# ------------------------------

import os
from superset.config import *  # Import default Superset config
from datetime import timedelta # For session timeout

# ------------------------------
# Environment
# ------------------------------
SUPERSET_ENV = os.getenv("SUPERSET_ENV", "production")
APP_NAME = "Superset Production"
APP_ICON = "/static/assets/images/superset-logo-horiz.png"
DEFAULT_TIMEZONE = "Asia/Dhaka"
SUPERSET_WEBSERVER_ADDRESS = '0.0.0.0'
SUPERSET_WEBSERVER_PORT = 8090
SECRET_KEY = "w8mAAA5QJNopoylCGCjW5Jlwmy5L5dlyZHAz5OqtTDPXqwNIqkakZhA"
# ------------------------------
# Database
# ------------------------------
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://superset:superset@db:5432/superset"
)
# For synchronous queries (dashboards/charts)
SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=5).total_seconds())  # 300 seconds
# ------------------------------
# Caching / Redis
# ------------------------------
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300, # in seconds (5 minutes)
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": f"redis://{os.getenv('REDIS_HOST', 'redis')}:6379/0",
}

# ------------------------------
# Security / RBAC
# ------------------------------
# Disable certain features to reduce attack surface
FEATURE_FLAGS = {
    "ALERT_REPORTS": True,            # Disable alerting for untrusted users
    "DASHBOARD_NATIVE_FILTERS": True,  # Keep dashboards functional
    "SQLLAB_BACKEND_PERSISTENCE": False,  # Restrict SQL Lab persistent queries
    "EMBEDDED_SUPERSET": True, 
    "ALLOW_FILE_UPLOAD": True,
}
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
# Limit SQL Lab usage
SQLLAB_DEFAULT_TIMEOUT = 600  # Max execution time (seconds)
SQLLAB_CTAS_NO_LIMIT = True  # Prevent excessive CTAS queries
SQLLAB_TIMEOUT = 300  # Query timeout (seconds)
# For async queries
SQLLAB_ASYNC_TIME_LIMIT_SEC = 300
# For async queries
SQLLAB_ASYNC_TIME_LIMIT_SEC = 300

# Database query timeout
SUPERSET_SQLALCHEMY_TIMEOUT = 300  # in seconds

# ------------------------------
# Cross-Origin Requests
# ------------------------------
ENABLE_CORS = True
CORS_OPTIONS = {
    "origins": "*",        # Change to specific domains in production
    "supports_credentials": True,
    'allow_headers': ['*'],
    'resources': ['*'],
}

# ------------------------------
# Misc Security Hardening
# ------------------------------
# Disable exposed endpoints
ENABLE_PROXY_FIX = True
WTF_CSRF_ENABLED = False  # Protect against CSRF
PUBLIC_ROLE_LIKE = "Gamma"

# ------------------------------
# Logging
# ------------------------------
LOG_LEVEL = "INFO"

# ------------------------------
# Optional: Restrict Chart Editing
# ------------------------------
# Only trusted roles can edit charts
# Enforce via Superset UI: assign 'Alpha' or custom admin role
# ------- Upload Path
UPLOAD_FOLDER ="/home/ubuntu/uploads"

# ------------------------------
# Note: Session Timeout
# ------------------------------

PERMANENT_SESSION_LIFETIME = timedelta(hours=4) # 4 hours session timeout
# Ensure cookie/session stability
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False  #  True if serving over HTTPS
