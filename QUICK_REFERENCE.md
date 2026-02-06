# 🚀 QUICK DEPLOYMENT REFERENCE CARD

## 📌 Print This or Save to Phone!

---

## ⚡ 30-Second Quick Start

```bash
# 1. Open terminal/PowerShell in project folder
# 2. Windows users: run start-dev.bat
# 3. macOS/Linux users: chmod +x start-dev.sh && ./start-dev.sh
# 4. Open http://localhost:5000
# Done! ✅
```

---

## 🌐 Deployment Platforms (Pick One)

### **FASTEST** ⭐ Heroku
```bash
heroku login
heroku create my-app-name
heroku config:set SECRET_KEY=random-secret-here
git push heroku main
# App live in 2 minutes!
```

### **EASY** ⚡ Render or Railway
- Push code to GitHub
- Connect GitHub repo at render.com (or railway.app)
- Set environment variables
- Deploy! (takes 5 minutes)

### **BEST CONTROL** 🔧 VPS (DigitalOcean, AWS, etc.)
```bash
chmod +x deploy-production.sh
./deploy-production.sh
# Sets up everything automatically
```

---

## 🔑 Essential Commands

```bash
# Start locally
python wsgi.py

# Start with Gunicorn (production)
gunicorn -c gunicorn_config.py wsgi:app

# Verify deployment
python health_check.py
python verify_deployment.py

# Check health online
curl https://your-app.com/api/health

# View logs (Heroku)
heroku logs --tail

# View logs (VPS)
tail -f logs/app.log
```

---

## 📋 Pre-Deployment Checklist

- [ ] Run `python health_check.py` locally
- [ ] Copy `.env.example` to `.env`
- [ ] Edit `.env` with your settings:
  - [ ] Change `SECRET_KEY` to random string
  - [ ] Set `FLASK_ENV=production`
- [ ] Test locally: `python wsgi.py`
- [ ] Access http://localhost:5000
- [ ] Commit changes: `git add . && git commit -m "Add deployment config"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Choose deployment platform from above
- [ ] Follow platform-specific steps
- [ ] Monitor `/api/health` endpoint

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port already in use | Kill process: `lsof -i :5000` then `kill -9 <PID>` |
| Module not found | Reinstall: `pip install -r requirements-prod.txt` |
| Static files missing | Check: `ls -la static/` |
| App won't start | Run: `python health_check.py` |
| env not loading | Create `.env` from `.env.example` |

---

## 🎯 After Deployment

```bash
# Test it
curl https://your-app.com/api/health

# Monitor it
heroku logs --tail  # For Heroku
tail -f logs/app.log  # For VPS

# Scale it (if needed)
heroku ps:scale web=2  # Add more dynos
```

---

## 📁 Important Files

| File | What It Does |
|------|--------------|
| `wsgi.py` | Entry point (production) |
| `config.py` | Settings (dev/prod) |
| `.env` | Your secrets (don't commit!) |
| `requirements-prod.txt` | Dependencies |
| `Procfile` | Heroku config |
| `gunicorn_config.py` | Server tuning |

---

## 🚨 DO NOT

- ❌ Commit `.env` to Git
- ❌ Push with `DEBUG=True` in production
- ❌ Use weak SECRET_KEY
- ❌ Ignore security warnings
- ❌ Skip HTTPS in production

---

## ✅ DO

- ✅ Use strong SECRET_KEY (32+ chars)
- ✅ Test locally before deploying
- ✅ Use HTTPS in production
- ✅ Monitor logs regularly
- ✅ Keep backups
- ✅ Update dependencies

---

## 📞 Quick Commands

```bash
# Generate strong secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Test if app works
python -c "from api import create_app; app = create_app(); print('OK')"

# List dependencies
pip list | grep -E "(Flask|gunicorn|pandas)"

# Check if port is available
netstat -tuln | grep 5000  # Linux/macOS
netstat -ano | findstr :5000  # Windows
```

---

## 🌍 Production URL Format

```
https://your-app-name.herokuapp.com         # Heroku
https://your-app-name.onrender.com          # Render
https://your-app-name.railway.app           # Railway
https://your-domain.com                     # Custom domain
```

---

## 💡 Pro Tips

1. **Always test locally first**
   - `python wsgi.py` and visit http://localhost:5000

2. **Use environment variables**
   - Never hardcode secrets
   - Different `.env` per environment

3. **Monitor immediately**
   - Set up logs from day 1
   - Watch for errors

4. **Keep it simple**
   - Don't over-engineer
   - Deploy often, fix fast

5. **Version your deployments**
   - Tag releases: `git tag v1.0.0`
   - Easy rollback if needed

---

## 📚 Learn More

- Flask: https://flask.palletsprojects.com
- Gunicorn: https://docs.gunicorn.org
- Heroku: https://devcenter.heroku.com
- Render: https://render.com/docs
- See full guides in:
  - `DEPLOYMENT_GUIDE.md`
  - `PRODUCTION_READY.md`
  - `SETUP_SUMMARY.md`

---

## 🎉 You're Ready!

Everything is configured. Choose your deployment method above and go!

**Need help?** Run: `python health_check.py`

**Questions?** See: `DEPLOYMENT_GUIDE.md` or `PRODUCTION_READY.md`

---

**Made for fast, reliable, production-ready deployment** 🚀
