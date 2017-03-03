from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^about$', views.about, name='about'),
    url(r'^archive$', views.archive, name='archive'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^projects$', views.project_list, name='project_list'),
    #url(r'', include('Trivia.urls')),
    #url(r'', include('BrewLogger.urls')),
    ]
