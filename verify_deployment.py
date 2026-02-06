# Quick test to verify deployment setup

import sys
from pathlib import Path

print("=" * 60)
print("Deployment Verification Checklist")
print("=" * 60)
print()

# Check Python version
import sys
py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
print(f"✓ Python version: {py_version}")
if sys.version_info < (3, 8):
    print("  ✗ WARNING: Python 3.8+ recommended")
print()

# Check required packages
required_packages = {
    'flask': 'Flask',
    'flask_cors': 'Flask-CORS',
    'pandas': 'Pandas',
    'nltk': 'NLTK',
    'sklearn': 'Scikit-learn',
    'dotenv': 'python-dotenv',
}

print("Checking dependencies...")
missing = []
for module, name in required_packages.items():
    try:
        __import__(module)
        print(f"  ✓ {name}")
    except ImportError:
        print(f"  ✗ {name} - MISSING")
        missing.append(module)

if missing:
    print()
    print("Install missing packages with:")
    print(f"  pip install {' '.join(missing)}")
    print()

# Check file structure
print()
print("Checking project structure...")
files_to_check = [
    'wsgi.py',
    'api.py',
    'config.py',
    'requirements-prod.txt',
    'templates/index.html',
    'templates/analyze.html',
    'static/css/style.css',
    'static/js/app.js',
]

for file in files_to_check:
    if Path(file).exists():
        print(f"  ✓ {file}")
    else:
        print(f"  ✗ {file} - MISSING")

# Test Flask app creation
print()
print("Testing Flask app creation...")
try:
    from api import create_app
    app = create_app('production')
    print(f"  ✓ Flask app created successfully")
    print(f"  ✓ Debug mode: {app.debug}")
    print(f"  ✓ Testing mode: {app.testing}")
except Exception as e:
    print(f"  ✗ Failed to create app: {e}")

# Check .env
print()
print("Environment configuration...")
if Path('.env').exists():
    print("  ✓ .env file exists")
else:
    print("  ⚠ .env file not found - copy from .env.example")

print()
print("=" * 60)
print("Deployment Ready!")
print("=" * 60)
print()
print("To run locally:")
print("  python wsgi.py")
print()
print("To run with Gunicorn (production):")
print("  gunicorn -c gunicorn_config.py wsgi:app")
print()
print("For more info, see DEPLOYMENT_GUIDE.md")
print()
