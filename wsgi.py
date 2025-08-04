# vercel_app/wsgi.py
import os
import sys

# Add the project directory to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from ecommerce_backend.wsgi import application

# Vercel expects the WSGI application to be named "app"
app = application