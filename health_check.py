#!/usr/bin/env python3
"""
Health check and diagnostics for Flask application
Usage: python health_check.py [--verbose]
"""

import sys
import json
from pathlib import Path

try:
    import requests
except ImportError:
    print("Installing requests...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

def check_app_startup():
    """Check if app starts successfully"""
    print("\n📊 App Startup Test...")
    try:
        from api import create_app
        app = create_app('testing')
        
        # Create test client
        client = app.test_client()
        
        # Test health endpoint
        response = client.get('/api/health')
        if response.status_code == 200:
            print("  ✓ Health endpoint works")
            return True
        else:
            print(f"  ✗ Health endpoint returned {response.status_code}")
            return False
    except Exception as e:
        print(f"  ✗ App startup failed: {e}")
        return False

def check_endpoints():
    """Check main API endpoints"""
    print("\n🔗 Endpoint Test...")
    try:
        from api import create_app
        app = create_app('testing')
        client = app.test_client()
        
        endpoints = [
            ('/', 'GET'),
            ('/api/health', 'GET'),
            ('/api/stats', 'GET'),
            ('/api/causes', 'GET'),
            ('/api/signals', 'GET'),
            ('/api/warnings', 'GET'),
            ('/analyze', 'GET'),
        ]
        
        for path, method in endpoints:
            try:
                if method == 'GET':
                    response = client.get(path)
                else:
                    response = client.post(path)
                
                status = "✓" if response.status_code < 400 else "⚠"
                print(f"  {status} {method:6} {path:30} -> {response.status_code}")
            except Exception as e:
                print(f"  ✗ {method:6} {path:30} -> Error: {str(e)[:30]}")
        
        return True
    except Exception as e:
        print(f"  ✗ Endpoint test failed: {e}")
        return False

def check_static_files():
    """Check if static files exist"""
    print("\n📁 Static Files Check...")
    files = [
        'static/css/style.css',
        'static/js/app.js',
        'static/js/charts.js',
        'static/js/analyze.js',
    ]
    
    all_good = True
    for file in files:
        if Path(file).exists():
            size = Path(file).stat().st_size
            print(f"  ✓ {file:40} ({size:,} bytes)")
        else:
            print(f"  ✗ {file:40} - MISSING")
            all_good = False
    
    return all_good

def check_templates():
    """Check if templates exist"""
    print("\n🎨 Template Files Check...")
    templates = [
        'templates/index.html',
        'templates/analyze.html',
    ]
    
    all_good = True
    for file in templates:
        if Path(file).exists():
            size = Path(file).stat().st_size
            print(f"  ✓ {file:40} ({size:,} bytes)")
        else:
            print(f"  ✗ {file:40} - MISSING")
            all_good = False
    
    return all_good

def check_config():
    """Check configuration"""
    print("\n⚙️  Configuration Check...")
    try:
        from config import Config, DevelopmentConfig, ProductionConfig
        print(f"  ✓ Config classes loaded")
        print(f"    - Base config: Secret key set: {bool(Config.SECRET_KEY)}")
        print(f"    - Development: Debug={DevelopmentConfig.DEBUG}")
        print(f"    - Production: Debug={ProductionConfig.DEBUG}")
        return True
    except Exception as e:
        print(f"  ✗ Config check failed: {e}")
        return False

def main():
    """Run all checks"""
    print("=" * 70)
    print("  Flask Application Health & Deployment Readiness Check")
    print("=" * 70)
    
    checks = [
        ("Configuration", check_config),
        ("Templates", check_templates),
        ("Static Files", check_static_files),
        ("App Startup", check_app_startup),
        ("Endpoints", check_endpoints),
    ]
    
    results = {}
    for name, check_func in checks:
        try:
            results[name] = check_func()
        except Exception as e:
            print(f"\n❌ {name} check failed: {e}")
            results[name] = False
    
    # Summary
    print("\n" + "=" * 70)
    print("  Summary")
    print("=" * 70)
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    
    for name, result in results.items():
        status = "✓" if result else "✗"
        print(f"  {status} {name}")
    
    print(f"\n  Result: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n  ✅ Application is deployment-ready!")
        print("\n  Next steps:")
        print("    1. Test locally: python wsgi.py")
        print("    2. Deploy to platform (Heroku, Render, etc.)")
        print("    3. Monitor with: tail -f logs/app.log")
        return 0
    else:
        print("\n  ⚠️  Some checks failed. Review errors above.")
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
