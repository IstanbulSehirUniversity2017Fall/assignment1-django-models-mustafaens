from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_name>[a-z]+)/$', views.football, name='football'),
]
