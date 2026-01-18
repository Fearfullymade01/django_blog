#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from django.template import loader
from blog.models import Post

try:
    template = loader.get_template('blog/index.html')
    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'post_list': posts,
        'is_paginated': False,
        'page_obj': None,
    }
    rendered = template.render(context)
    print("Template rendered successfully")
    print(f"Rendered length: {len(rendered)} characters")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
