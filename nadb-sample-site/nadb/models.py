from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique_for_date='published')
    body = models.TextField('body')
    published = models.DateTimeField('published', default=datetime.datetime.now)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)