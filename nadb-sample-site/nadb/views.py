from django.views.generic import list_detail, date_based
from models import Post

def post_list(request, page=0, paginate_by=3):

    return list_detail.object_list(
        request,
        queryset=Post.objects.published(),
        paginate_by=paginate_by,
        page=page
    )
    
def post_detail(request, year, month, day, slug):
    return date_based.object_detail(
        request,
        year=year,
        month=month,
        day=day,
        slug=slug,
        date_field='published',
        queryset=Post.objects.published(),
    )
    