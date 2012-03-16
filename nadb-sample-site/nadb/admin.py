from django.contrib import admin
from models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description',]
  
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','status',]

admin.site.register(Category, CategoryAdmin)  
admin.site.register(Post, PostAdmin)