from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('nadb.views',
    url(r'^$', view='post_list', name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', view='post_detail', name='post_detail'),
    url(r'^(?P<year>\d{4})/$', view='post_archive_year', name='post_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', view='post_archive_month', name='post_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$', view='post_archive_day', name='post_archive_day'),
    url(r'^categories/$', view='category_list', name='category_list'),
    url(r'^categories/(?P<slug>[-\w]+)/$', view='category_detail', name='category_detail'),
)