from django.db.models import Manager
import datetime

class PostManager(Manager):
    def published(self):
        return self.get_query_set().filter(status='p')
        
