from django.db import models
import datetime
from django.db.models import permalink
from managers import PostManager

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
)

class Category(models.Model):
    name = models.CharField('name', max_length=100)
    slug = models.SlugField('slug', unique=True)
    description = models.TextField('description')
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    @permalink
    def get_absolute_url(self):
        return ('category_detail', None, {
            'slug': self.slug
        })
    
    def __unicode__(self):
        return u'%s' % self.name
    
            
class Post(models.Model):
    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique_for_date='published')
    body = models.TextField('body')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    published = models.DateTimeField('published', default=datetime.datetime.now)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    objects = PostManager()
    
    @permalink
    def get_absolute_url(self):
        return ('post_detail', None, {
            'year': self.published.year,
            'month': self.published.strftime('%b').lower(),
            'day': self.published.day,
            'slug': self.slug
        })