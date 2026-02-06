#!/bin/bash
# Production deployment script (for VPS/Linux)

set -e  # Exit on error

APP_DIR="/var/www/flask-app"
APP_NAME="flask-chat-analysis"
PYTHON_VERSION="3.10"

echo "================================================"
echo " Deploying Causal Chat Analysis to Production"
echo "================================================"
echo ""

# Install system dependencies (Ubuntu/Debian)
echo "Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-venv \
    python${PYTHON_VERSION}-dev \
    git \
    nginx \
    supervisor

# Create app directory
echo "Creating application directory..."
sudo mkdir -p $APP_DIR
cd $APP_DIR

# Clone repository (or pull if already exists)
if [ -d ".git" ]; then
    echo "Updating repository..."
    sudo git pull origin main
else
    echo "Cloning repository..."
    sudo git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git .
fi

# Create virtual environment
echo "Creating Python virtual environment..."
sudo python${PYTHON_VERSION} -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
sudo pip install --upgrade pip
sudo pip install -r requirements-prod.txt

# Create .env from template
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    sudo cp .env.example .env
    echo "WARNING: Please edit .env with production settings!"
fi

# Create logs directory
sudo mkdir -p logs
sudo chown www-data:www-data logs

# Configure Supervisor for process management
echo "Configuring Supervisor..."
sudo tee /etc/supervisor/conf.d/flask-app.conf > /dev/null <<EOF
[program:$APP_NAME]
directory=$APP_DIR
command=$APP_DIR/venv/bin/gunicorn \\
    --workers=4 \\
    --worker-class=sync \\
    --bind=unix:/tmp/flask.sock \\
    --timeout=60 \\
    --access-logfile=logs/access.log \\
    --error-logfile=logs/error.log \\
    wsgi:app
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=logs/app.log
EOF

# Configure Nginx
echo "Configuring Nginx..."
sudo tee /etc/nginx/sites-available/$APP_NAME > /dev/null <<'EOF'
server {
    listen 80;
    server_name _;
    client_max_body_size 16M;

    location / {
        proxy_pass http://unix:/tmp/flask.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 60;
        proxy_send_timeout 60;
        proxy_read_timeout 60;
    }

    location /static {
        alias $APP_DIR/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# Enable Nginx site
sudo ln -sf /etc/nginx/sites-available/$APP_NAME /etc/nginx/sites-enabled/$APP_NAME
sudo rm -f /etc/nginx/sites-enabled/default

# Test Nginx config
echo "Testing Nginx configuration..."
sudo nginx -t

# Start services
echo "Starting services..."
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start $APP_NAME
sudo systemctl restart nginx

echo ""
echo "================================================"
echo " Deployment Complete!"
echo "================================================"
echo ""
echo "Application running at: http://localhost"
echo ""
echo "Useful commands:"
echo "  View logs:        tail -f $APP_DIR/logs/app.log"
echo "  Restart app:      sudo supervisorctl restart $APP_NAME"
echo "  App status:       sudo supervisorctl status $APP_NAME"
echo "  Nginx logs:       sudo tail -f /var/log/nginx/error.log"
echo ""
