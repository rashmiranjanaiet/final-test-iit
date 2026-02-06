"""
WSGI entry point for production deployment
Compatible with Gunicorn, uWSGI, and other WSGI servers

Usage:
    Development:  python wsgi.py
    Production:   gunicorn -c gunicorn_config.py wsgi:app
                  gunicorn --workers=4 --worker-class=sync wsgi:app
"""

import os
import sys
from pathlib import Path
import logging

# Setup paths
BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR))

# Ensure logs directory exists
logs_dir = BASE_DIR / 'logs'
logs_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(logs_dir / 'wsgi.log', mode='a')
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / '.env')
    logger.info("Environment variables loaded from .env")
except ImportError:
    logger.warning("python-dotenv not installed, skipping .env loading")
except FileNotFoundError:
    logger.info("No .env file found, using system environment variables")

# Import Flask app factory
try:
    from api import create_app
    logger.info("API module imported successfully")
except ImportError as e:
    logger.error(f"Failed to import API module: {e}")
    sys.exit(1)

# Create and configure the app based on environment
flask_env = os.getenv('FLASK_ENV', 'production')
logger.info(f"Creating Flask app with environment: {flask_env}")

try:
    app = create_app(flask_env)
    logger.info(f"Flask app created successfully (Debug: {app.debug})")
except Exception as e:
    logger.error(f"Failed to create Flask app: {e}")
    sys.exit(1)

# Verify app is properly configured
if not app:
    logger.error("Flask app creation returned None")
    sys.exit(1)

logger.info("=" * 60)
logger.info("WSGI Application Ready")
logger.info("=" * 60)
logger.info(f"Environment: {flask_env}")
logger.info(f"Debug mode: {app.debug}")
logger.info(f"Testing mode: {app.testing}")
logger.info(f"Secret key configured: {bool(app.config.get('SECRET_KEY'))}")
logger.info("=" * 60)


# Only run development server if executed directly
# Production uses: gunicorn -c gunicorn_config.py wsgi:app
if __name__ == '__main__':
    import threading
    
    logger.info("Starting Flask development server...")
    logger.info("For production, use: gunicorn -c gunicorn_config.py wsgi:app")
    
    # Start background data loading
    def load_data_background():
        logger.info("Background: Starting data loading...")
        try:
            from api import load_data
            load_data()
            logger.info("Background: Data loading complete")
        except Exception as e:
            logger.error(f"Background data loading failed: {e}")
    
    # Load data in background to avoid blocking startup
    loader_thread = threading.Thread(target=load_data_background, daemon=True)
    loader_thread.start()
    
    # Run development server
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000)),
        debug=(flask_env == 'development'),
        use_reloader=(flask_env == 'development'),
        threaded=True
    )

