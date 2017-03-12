from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^Trivia(?:/(?P<show_all>[a-zA-Z]+))?/$', views.game_list, name='game_list'),
    url(r'^Trivia/game(?P<pk>\d+)/$', views.game_detail, name='game_detail'),
    url(r'^Trivia/game(?P<game_pk>\d+)/round(?P<pk>\d+)/$', views.round_detail, name='round_detail'),
]
