#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from blog.views import PostList
from django.test import RequestFactory

factory = RequestFactory()
request = factory.get('/')

try:
    view = PostList.as_view()
    response = view(request)
    print(f"Response status: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
