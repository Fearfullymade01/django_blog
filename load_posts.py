import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from blog.models import Post
from django.contrib.auth.models import User

# Load posts from JSON
with open('blog/fixtures/posts.json', 'r') as f:
    data = json.load(f)

for item in data:
    if item['model'] == 'blog.post':
        fields = item['fields']
        author = User.objects.get(pk=fields['author'])
        
        post, created = Post.objects.get_or_create(
            pk=item['pk'],
            defaults={
                'title': fields['title'],
                'slug': fields['slug'],
                'author': author,
                'content': fields['content'],
                'excerpt': fields['excerpt'],
                'status': fields['status'],
            }
        )
        
        if created:
            print(f"Created post: {post.title}")
        else:
            print(f"Post already exists: {post.title}")

print("Done!")
