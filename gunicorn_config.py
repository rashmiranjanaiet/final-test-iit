"""
Quick production server startup using Gunicorn
Run this with: gunicorn -c gunicorn_config.py wsgi:app
"""

import os
import multiprocessing

# Server socket
bind = os.environ.get('BIND', '0.0.0.0:5000')
backlog = 2048

# Worker processes
workers = int(os.environ.get('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))
worker_class = os.environ.get('GUNICORN_WORKER_CLASS', 'sync')
worker_connections = 1000
timeout = 60
keepalive = 2

# Logging
accesslog = os.environ.get('ACCESSLOG', 'logs/access.log')
errorlog = os.environ.get('ERRORLOG', 'logs/error.log')
loglevel = os.environ.get('LOG_LEVEL', 'info')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'causal-chat-analysis'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (for production with HTTPS)
# keyfile = '/path/to/keyfile.key'
# certfile = '/path/to/certfile.crt'
# ssl_version = 'TLSv1_2'

# Application defaults
preload_app = False
raw_env = [
    'FLASK_ENV=production',
]

# Create logs directory if needed
os.makedirs('logs', exist_ok=True)
