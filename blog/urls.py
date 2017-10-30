from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^news$', views.news, name='news'),
    url(r'^internet$', views.internet, name='internet'),
    url(r'^apps_games$', views.apps_games, name='apps_games'),
    url(r'^entrepreneur$', views.entrepreneur, name='entrepreneur'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]