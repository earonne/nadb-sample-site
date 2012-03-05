from django.db import models
import datetime
from django.db.models import permalink

class Post(models.Model):
    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique_for_date='published')
    body = models.TextField('body')
    published = models.DateTimeField('published', default=datetime.datetime.now)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    
    @permalink
    def get_absolute_url(self):
        return ('post_detail', None, {
            'year': self.published.year,
            'month': self.published.strftime('%b').lower(),
            'day': self.published.day,
            'slug': self.slug
        })