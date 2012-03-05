from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('nadb.views',
    url(r'^$', 'post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', view='post_detail', name='post_detail'),
)