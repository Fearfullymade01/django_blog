#!/usr/bin/env python
import os
import sys
import django

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')

# Setup Django
sys.path.insert(0, r'C:\Users\gbeng\codestar_blog')
django.setup()

# Now check admin registry
from django.contrib import admin
from blog.models import Comment, Post

print("=" * 60)
print("ADMIN REGISTRATION CHECK")
print("=" * 60)
print(f"Post registered: {Post in admin.site._registry}")
print(f"Comment registered: {Comment in admin.site._registry}")
print("\nRegistered models in admin:")
for model, admin_class in admin.site._registry.items():
    print(f"  - {model.__name__}")
print("=" * 60)
