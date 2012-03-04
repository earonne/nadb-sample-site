from django.views.generic import list_detail
from models import Post

def post_list(request, page=0, paginate_by=20):

    return list_detail.object_list(
        request,
        queryset=Post.objects.all(),
        paginate_by=paginate_by,
        page=page
    )