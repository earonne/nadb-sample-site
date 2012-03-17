from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from models import Post

class PostFeed(Feed):
    title = 'My Blog feed'
    description = 'My Blog posts feed'
    
    def link(self):
        return reverse('post_list')
            
    def items(self):
        return Post.objects.published()[:10]
    
    def item_title(self, obj):
        return obj.title

    def item_description(self, obj):
        return obj.body
        
    def item_pubdate(self, obj):
        return obj.published