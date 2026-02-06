# ✅ DEPLOYMENT CHECKLIST

Use this checklist to ensure everything is ready before deployment.

---

## 📋 Pre-Deployment Phase

### Setup & Verification
- [ ] Cloned/downloaded project
- [ ] Python 3.8+ installed: `python --version`
- [ ] All files created (check below)
- [ ] Run `python health_check.py` - all checks pass
- [ ] Run `python verify_deployment.py` - all checks pass

### Files Created
- [ ] `wsgi.py` - WSGI entry point
- [ ] `config.py` - Configuration classes
- [ ] `.env.example` - Environment template
- [ ] `Procfile` - Heroku deployment
- [ ] `runtime.txt` - Python version
- [ ] `requirements-prod.txt` - Dependencies
- [ ] `gunicorn_config.py` - Gunicorn config
- [ ] `start-dev.bat` - Windows startup
- [ ] `start-dev.sh` - Linux/macOS startup
- [ ] `DEPLOYMENT_GUIDE.md` - Full guide
- [ ] `PRODUCTION_READY.md` - Quick ref
- [ ] `SETUP_SUMMARY.md` - Summary
- [ ] `QUICK_REFERENCE.md` - This card
- [ ] `health_check.py` - Health check
- [ ] Existing `api.py` - Modified with `create_app()`

### Code Updates
- [ ] `api.py` has `create_app()` function
- [ ] `api.py` has health endpoint: `/api/health`
- [ ] `api.py` imports from `config.py`
- [ ] Flask app configuration is environment-aware

---

## 🔐 Security Configuration

### Secrets & Keys
- [ ] Created `.env` file from `.env.example`
- [ ] Generated strong SECRET_KEY: `python -c "import secrets; print(secrets.token_urlsafe(32))"`
- [ ] SECRET_KEY is **30+ characters**
- [ ] SECRET_KEY is **NOT hardcoded** in any Python file
- [ ] No secrets in `.gitignore` (checked: `git check-ignore .env`)

### Environment Variables
- [ ] Set `FLASK_ENV=production` in `.env`
- [ ] Set `SECRET_KEY` to a random, strong value
- [ ] Set `PORT=5000` (or your port)
- [ ] Set `HOST=0.0.0.0` for external access
- [ ] Reviewed all variables in `.env.example`

### File Permissions
- [ ] `.env` file permissions: `chmod 600 .env` (owners only)
- [ ] Executable scripts have permissions: `chmod +x *.sh`
- [ ] static/ directory is readable: `chmod -r 755 static/`
- [ ] logs/ directory is writable: `chmod 755 logs/`

---

## 🔍 Local Testing

### Basic Functionality
- [ ] Installed dependencies: `pip install -r requirements-prod.txt`
- [ ] No import errors: `python -c "from api import create_app; print('OK')"`
- [ ] App creates successfully: `python -c "from api import create_app; app = create_app('production'); print('OK')"`

### Running Locally
- [ ] Started with `python wsgi.py`
- [ ] Accessible at http://localhost:5000
- [ ] Health check works: http://localhost:5000/api/health
- [ ] Dashboard loads: http://localhost:5000/
- [ ] No errors in console
- [ ] No 404s on main pages
- [ ] Static files load (CSS, JS)

### Testing with Production Settings
- [ ] Set `FLASK_ENV=production` and test locally
- [ ] Verify no DEBUG output
- [ ] Confirm error handling works
- [ ] No sensitive data in error messages

---

## 📦 Dependencies

### Installation
- [ ] Ran `pip install -r requirements-prod.txt`
- [ ] No dependency conflicts
- [ ] All required modules available:
  - [ ] flask
  - [ ] flask-cors
  - [ ] pandas
  - [ ] numpy
  - [ ] nltk
  - [ ] scikit-learn
  - [ ] gunicorn

### Version Compatibility
- [ ] Python: 3.8+  (currently: _____)
- [ ] Flask: 2.3.0+
- [ ] Gunicorn: 20.1.0+
- [ ] All dependencies in `requirements-prod.txt`

---

## 📝 Git & Repository

### Code Configuration
- [ ] No hardcoded secrets in code
- [ ] No database credentials in code
- [ ] No API keys in code
- [ ] `.gitignore` includes `.env`
- [ ] `.gitignore` includes `logs/`
- [ ] `.gitignore` includes `__pycache__/`
- [ ] `.gitignore` includes `*.pyc`

### Git Status
- [ ] All changes committed: `git status`
- [ ] No uncommitted changes
- [ ] Pushed to GitHub: `git push origin main`
- [ ] GitHub branch is up to date

---

## 🌐 Platform-Specific Checklists

### **For Heroku Deployment**
- [ ] Heroku account created
- [ ] Heroku CLI installed
- [ ] Logged in: `heroku login`
- [ ] `Procfile` configured correctly
- [ ] `runtime.txt` specifies Python 3.10
- [ ] App created: `heroku create app-name`
- [ ] Config vars set:
  - [ ] `FLASK_ENV=production`
  - [ ] `SECRET_KEY=<your-key>`
- [ ] Ready to push: `git push heroku main`

### **For Render Deployment**
- [ ] Render account created
- [ ] GitHub repo connected
- [ ] Build command set: `pip install -r requirements-prod.txt`
- [ ] Start command set: `gunicorn --workers=4 --worker-class=sync --bind=0.0.0.0:$PORT wsgi:app`
- [ ] Environment variables configured
- [ ] Ready to deploy from GitHub

### **For Self-Hosted VPS**
- [ ] Server OS: Ubuntu 20.04+ or CentOS 8+
- [ ] SSH access configured
- [ ] Domain name registered & configured
- [ ] SSL certificate (Let's Encrypt):
  - [ ] certbot installed
  - [ ] Certificate generated
- [ ] Ran `deploy-production.sh`
  - [ ] All components installed
  - [ ] Supervisor configured
  - [ ] Nginx configured
  - [ ] Services started

---

## 🚀 Pre-Launch Final Check

### Functionality
- [ ] Homepage loads correctly
- [ ] Dashboard displays data
- [ ] /api/health endpoint works
- [ ] API endpoints respond
- [ ] Static files load (CSS, JS, images)
- [ ] Responsive design works on mobile
- [ ] Form submissions work (if applicable)
- [ ] Error pages display properly

### Performance
- [ ] Page loads in <3 seconds
- [ ] Static files cached properly
- [ ] No console errors (DevTools)
- [ ] No 404 errors
- [ ] No CORS errors
- [ ] Database queries optimized

### Security
- [ ] No DEBUG=True in production
- [ ] HTTPS enabled and working
- [ ] Certificate is valid and trusted
- [ ] CORS properly configured
- [ ] Security headers present
- [ ] No sensitive data in logs or responses

### Monitoring & Logs
- [ ] Logs directory writable: `logs/`
- [ ] Logging is configured
- [ ] Error logging works
- [ ] Access logging works
- [ ] Alert system (if applicable) configured

---

## ✨ Launch & Post-Launch

### Deployment
- [ ] Deployed successfully to chosen platform
- [ ] App is running and accessible
- [ ] Health check passes: `curl https://your-app.com/api/health`
- [ ] Dashboard works at https://your-app.com

### Monitoring
- [ ] Logs are being generated
- [ ] Errors being logged properly
- [ ] High-level monitoring set up (optional)
  - [ ] Error tracking (Sentry, etc.)
  - [ ] Uptime monitoring
  - [ ] Performance monitoring
  - [ ] Alert notifications

### Post-Launch
- [ ] Tested on different browsers
- [ ] Tested on mobile devices
- [ ] Tested from different networks
- [ ] Database backups set up
- [ ] Backup restoration tested
- [ ] Team notified of launch
- [ ] Documentation updated

---

## 🐛 Troubleshooting Issues Found

| Issue | Action Taken | Date |
|-------|--------------|------|
|       |              |      |
|       |              |      |
|       |              |      |

---

## 📋 Sign-Off

- **Prepared by:** _________________________
- **Date:** _________________________
- **Platform:** _________________________
- **App URL:** _________________________
- **Notes:**

```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## ✅ Ready for Production!

Once all checkboxes are marked, your deployment is ready! 🚀

For any issues:
1. Check `DEPLOYMENT_GUIDE.md`
2. Run `python health_check.py`
3. Review logs for errors
4. See `PRODUCTION_READY.md` for troubleshooting

---

**Happy deploying!** 🎉
