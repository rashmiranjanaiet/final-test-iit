# Flask Deployment Guide

## Quick Start - Local Development

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements-prod.txt
   ```

4. **Create `.env` file** (from `.env.example`)
   ```bash
   cp .env.example .env
   ```

5. **Run locally**
   ```bash
   python wsgi.py
   ```
   Visit: http://localhost:5000

---

## Production Deployment Options

### Option 1: Heroku (Easiest)

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=your-secure-key-here
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **View logs**
   ```bash
   heroku logs --tail
   ```

---

### Option 2: Render (Simple)

1. **Push code to GitHub**
2. **Create account at https://render.com**
3. **New Web Service → Connect GitHub repo**
4. **Configure:**
   - Build Command: `pip install -r requirements-prod.txt`
   - Start Command: `gunicorn --workers=4 --worker-class=sync --bind=0.0.0.0:$PORT wsgi:app`
   - Environment: Add `FLASK_ENV=production`, `SECRET_KEY=xxx`
5. **Deploy and done!**

---

### Option 3: DigitalOcean App Platform

1. **Connect GitHub repository**
2. **Create App → Python → Flask**
3. **Configure:**
   - Build: `pip install -r requirements-prod.txt`
   - Run: `gunicorn --workers=4 --bind=0.0.0.0:8080 wsgi:app`
4. **Set environment variables** in console
5. **Deploy**

---

### Option 4: Manual Server (VPS/Dedicated)

1. **Install Python & Gunicorn**
   ```bash
   sudo apt-get install python3 python3-pip
   pip3 install gunicorn
   ```

2. **Clone repository**
   ```bash
   git clone your-repo.git
   cd your-repo
   ```

3. **Install dependencies**
   ```bash
   pip3 install -r requirements-prod.txt
   ```

4. **Create systemd service** (`/etc/systemd/system/flask-app.service`)
   ```ini
   [Unit]
   Description=Flask Chat Analysis App
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/var/www/flask-app
   ExecStart=/usr/local/bin/gunicorn \
     --workers 4 \
     --worker-class sync \
     --bind unix:/tmp/flask.sock \
     wsgi:app

   [Install]
   WantedBy=multi-user.target
   ```

5. **Enable service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start flask-app
   sudo systemctl enable flask-app
   ```

6. **Configure Nginx as reverse proxy**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location / {
           proxy_pass http://unix:/tmp/flask.sock;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

---

## Important Security Checklist

✅ **Before Going Live:**
- [ ] Change `SECRET_KEY` in `.env`
- [ ] Set `FLASK_ENV=production`
- [ ] Enable HTTPS/SSL certificate
- [ ] Set `SECURE_SSL_REDIRECT=True`
- [ ] Use strong database credentials (if applicable)
- [ ] Enable CORS only for trusted domains
- [ ] Set up proper logging
- [ ] Regular backups of data
- [ ] Monitor application errors

---

## Monitoring & Logs

### View Logs
- **Heroku**: `heroku logs --tail`
- **Render**: Check dashboard
- **VPS**: `journalctl -u flask-app -f`

### Health Check
```bash
curl https://your-app.com/health
```

---

## Troubleshooting

### App Not Starting
```bash
# Check Python version
python --version

# Verify dependencies
pip list

# Test import
python -c "from api import create_app"
```

### Static Files Not Loading
- Ensure `SEND_FILE_MAX_AGE_DEFAULT` is set
- Verify `static/` directory exists
- Check file permissions

### CORS Issues
- Update `CORS(app)` in api.py with allowed origins
- Example: `CORS(app, origins=['https://yourdomain.com'])`

---

## Performance Tips

1. **Use CDN for static files** (CloudFlare, AWS CloudFront)
2. **Enable gzip compression** in reverse proxy
3. **Set proper cache headers** for static assets
4. **Use connection pooling** for databases
5. **Monitor with tools** like New Relic or DataDog
6. **Scale horizontally** with load balancer when needed

---

## Support

For issues, check:
- Flask docs: https://flask.palletsprojects.com
- Gunicorn docs: https://docs.gunicorn.org
- Your platform's documentation
