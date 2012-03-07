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
    
def post_archive_year(request, year):
    return date_based.archive_year(
        request,
        year=year,
        date_field='published',
        queryset=Post.objects.published(),
    )

def post_archive_month(request, year, month):
    return date_based.archive_month(
        request,
        year=year,
        month=month,
        date_field='published',
        queryset=Post.objects.published(),
    )

def post_archive_day(request, year, month, day):
    return date_based.archive_day(
        request,
        year=year,
        month=month,
        day=day,
        date_field='published',
        queryset=Post.objects.published(),
    )
