from django import template
from nadb.models import Category, Post
import re

register = template.Library()

class CategoriesNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name
        
    def render(self, context):
        categories = Category.objects.all()
        context[self.var_name] = categories
        return ''
        
@register.tag
def get_blog_categories(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return CategoriesNode(var_name)


class RecentPosts(template.Node):
    def __init__(self, limit, var_name):
        self.limit = int(limit)
        self.var_name = var_name

    def render(self, context):
        posts = Post.objects.published()[:self.limit]
        if posts and (self.limit == 1):
            context[self.var_name] = posts[0]
        else:
            context[self.var_name] = posts
        return ''

@register.tag
def get_recent_posts(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    limit, var_name = m.groups()
    return RecentPosts(limit, var_name)