from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('nadb.views',
    url(r'^$', 'post_list'),
)