#!/usr/bin/env python
"""
Script to add the About Me content to the database
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from about.models import About

# Clear any existing About entries
About.objects.all().delete()

# Create the About entry
about_content = """Gbenga was born and raised in the vibrant city of Lagos, Nigeria, where his character, resilience, and ambition were shaped from an early age. He completed his elementary, secondary, and tertiary education in Nigeria, earning a degree in Business Administration. Growing up in Lagos exposed him to diverse cultures, fast-paced living, and endless possibilities, instilling in him a strong work ethic and an unwavering drive to succeed.

With a deep passion for music, Gbenga spent over a decade in the music business as a musician, using creativity and sound as tools for expression and connection. That chapter of his life honed his artistic instincts, discipline, and understanding of human emotion. Over time, his curiosity and love for problem-solving led him to pivot into technology. Today, he thrives as a Cyber Security professional and Full-Stack Developer, applying creativity, structure, and innovation to building and securing digital solutions.

Gbenga is equally energized by an active and competitive lifestyle. His interests span a wide range of sports and entertainment, including martial arts, football, basketball, Formula One, golf, table tennis, lawn tennis, boxing, wrestling, athletic racing, and board games. These passions reflect his appreciation for strategy, endurance, precision, and teamwork—qualities that also define his approach to life and work.

During his years in Nigeria, Gbenga was regarded as an inspirational figure within his neighbourhoods in Lagos, motivating others through his journey, discipline, and mindset. He now lives in the United Kingdom, having moved to Birmingham over a year ago, where he continues to grow personally and professionally. At the heart of everything he does is a profound passion for the things of God, which anchors his values, fuels his purpose, and inspires his desire to impact lives positively. This blog is a window into that ongoing journey of faith, growth, and transformation."""

about = About.objects.create(
    title="About Gbenga Egbeyemi",
    content=about_content
)

print(f"About entry created successfully: {about.title}")
print(f"Updated on: {about.updated_on}")
