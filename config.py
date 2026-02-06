"""
Production Configuration for Flask Application
"""
import os
from pathlib import Path

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year for static files
    TEMPLATES_AUTO_RELOAD = False
    
    # API Configuration
    API_TIMEOUT = 30
    API_MAX_RETRIES = 3
    
    # Data paths
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
    OUTPUT_DIR = BASE_DIR / 'output'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True
    JSON_SORT_KEYS = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    # Security headers in production
    PREFERRED_URL_SCHEME = 'https'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False

# Load configuration based on environment
config_env = os.getenv('FLASK_ENV', 'development')
if config_env == 'production':
    config = ProductionConfig
elif config_env == 'testing':
    config = TestingConfig
else:
    config = DevelopmentConfig
