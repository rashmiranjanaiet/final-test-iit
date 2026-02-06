# PRODUCTION DEPLOYMENT READY

Your Flask application is now optimized for production deployment. Here's what's been configured:

## ✅ What's Included

### 1. **Production-Ready Files**
- `wsgi.py` - WSGI entry point for Gunicorn/uWSGI
- `config.py` - Environment-based configuration
- `.env.example` - Environment template
- `requirements-prod.txt` - Optimized production dependencies
- `Procfile` - Heroku deployment
- `runtime.txt` - Python version specification
- `gunicorn_config.py` - Gunicorn configuration
- `verify_deployment.py` - Deployment verification script

### 2. **Startup Scripts**
- `start-dev.bat` - Windows development startup
- `start-dev.sh` - Linux/macOS development startup
- `deploy-production.sh` - Full production deployment script

### 3. **Documentation**
- `DEPLOYMENT_GUIDE.md` - Comprehensive deployment guide
- `THIS FILE` - Quick reference

### 4. **Enhanced api.py**
- `create_app()` factory function for production
- Environment-aware configuration
- Background data loading
- Health check endpoint (`/api/health`)

---

## 🚀 Quick Start (Local Development)

### Windows
```bash
# Just run:
start-dev.bat
```

### macOS/Linux
```bash
# Make executable
chmod +x start-dev.sh

# Run
./start-dev.sh
```

**Then open:** http://localhost:5000

---

## 🌐 Deployment Options (Easiest to Hardest)

### **Option 1: Heroku** ⭐ (RECOMMENDED - Easiest)
```bash
heroku create your-app-name
heroku config:set SECRET_KEY=your-secret-here
git push heroku main
```
Takes 2 minutes. Free tier available.

### **Option 2: Render** ⚡ (Very Easy)
1. Push code to GitHub
2. Connect to Render.com
3. Set buildCommand: `pip install -r requirements-prod.txt`
4. Set startCommand: `gunicorn --workers=4 --worker-class=sync --bind=0.0.0.0:$PORT wsgi:app`
5. Deploy - Done!

### **Option 3: Railway** 🚂 (Easy)
Similar to Render - just connect GitHub and deploy.

### **Option 4: Manual VPS** 🔧 (Advanced)
```bash
./deploy-production.sh
```
This sets up Nginx, Supervisor, and Gunicorn on Linux.

---

## 📋 Pre-Deployment Checklist

Before deploying to production:

- [ ] Change `SECRET_KEY` in `.env`
- [ ] Set `FLASK_ENV=production`
- [ ] Review security settings in `config.py`
- [ ] Test locally: `python wsgi.py`
- [ ] Verify deployment: `python verify_deployment.py`
- [ ] Set up HTTPS/SSL certificate (recommended)
- [ ] Configure environment variables on platform
- [ ] Test health endpoint: `/api/health`

---

## 🔧 Environment Variables

Create a `.env` file (copy from `.env.example`):

```env
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
PORT=5000
HOST=0.0.0.0

# Optional security settings
SECURE_HSTS_SECONDS=31536000
SECURE_SSL_REDIRECT=False  # Set to True if using HTTPS
```

**For Heroku:**
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-key
heroku config:set SECURE_SSL_REDIRECT=True
```

---

## 📊 Server Specifications

**Recommended for production:**
- **Gunicorn workers**: CPU cores × 2 + 1 (auto-detected)
- **Worker class**: sync (for Flask compatibility)
- **Max upload size**: 16MB
- **Timeout**: 60 seconds
- **Memory**: ~200MB base + ~50MB per worker

---

## 🔍 Monitoring & Logs

### Local/Heroku
```bash
heroku logs --tail
```

### Manual Server
```bash
# View logs
tail -f logs/app.log

# View errors
tail -f logs/error.log

# Check app status
sudo supervisorctl status flask-app

# Restart app
sudo supervisorctl restart flask-app
```

### Health Check
```bash
curl https://your-app.com/api/health
# Response: {"success": true, "message": "API is running"}
```

---

## 🛡️ Security Best Practices

1. **Always use HTTPS in production**
   ```bash
   # Enable in config
   SECURE_SSL_REDIRECT=True
   SECURE_HSTS_SECONDS=31536000
   ```

2. **Use strong secret keys**
   ```python
   import secrets
   print(secrets.token_urlsafe(32))
   ```

3. **Restrict CORS**
   - Edit `api.py` CORS configuration
   - Only allow trusted domains

4. **Set secure cookies**
   - Already configured in `config.py`
   - SESSION_COOKIE_SECURE=True
   - SESSION_COOKIE_HTTPONLY=True

5. **Regular backups**
   - Back up `data/` folder regularly
   - Database credentials never in code

---

## ⚡ Performance Optimization Tips

1. **Use CDN for static files**
   - CloudFlare (free)
   - AWS CloudFront
   - BunnyCDN

2. **Enable gzip compression** (in Nginx/proxy)
   ```nginx
   gzip on;
   gzip_types text/css application/javascript;
   ```

3. **Cache static assets**
   - Already configured (1 year cache)
   - Set up CloudFlare

4. **Load balancing** (for scale)
   - Use Heroku Dyno scaling
   - Or load balancer like Nginx

5. **Database optimization** (if applicable)
   - Add indexes
   - Cache query results
   - Use connection pooling

---

## 🧪 Testing Deployment Locally

```bash
# Step 1: Install Gunicorn
pip install gunicorn

# Step 2: Test with Gunicorn (simulates production)
gunicorn -c gunicorn_config.py wsgi:app

# Step 3: Verify health
curl http://localhost:5000/api/health

# Step 4: Access dashboard
# Open http://localhost:5000
```

---

## 🚨 Troubleshooting

### App doesn't start
```bash
# Check Python version
python --version

# Verify imports
python -c "from api import create_app; print('OK')"

# Check dependencies
pip list
```

### Static files not loading
- Verify `static/` directory exists
- Check file permissions: `chmod -R 755 static/`
- Nginx: ensure alias path is correct

### Database connection error
- Check `.env` database credentials
- Verify database is running
- Test connection: `python -c "from src.load_data import load_transcripts; print(load_transcripts())"`

### Port already in use
```bash
# Windows
netstat -ano | findstr :5000

# Linux/macOS
lsof -i :5000

# Kill process on port 5000:
# Windows: taskkill /PID <PID> /F
# Linux/macOS: kill -9 <PID>
```

---

## 📞 Support & Resources

- **Flask Docs**: https://flask.palletsprojects.com
- **Gunicorn Docs**: https://docs.gunicorn.org
- **Heroku Docs**: https://devcenter.heroku.com
- **Render Docs**: https://render.com/docs
- **Python Docs**: https://docs.python.org/3/

---

## ✨ Next Steps

1. **Test locally**: `python wsgi.py` or `start-dev.bat`
2. **Verify setup**: `python verify_deployment.py`
3. **Choose platform**: See deployment options above
4. **Deploy**: Follow platform-specific steps
5. **Monitor**: Check logs and health endpoint

---

**Happy deploying! 🎉**

For detailed instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
