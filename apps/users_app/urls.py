from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #takes us to index
    url(r'^users/(?P<id>\d+)$', views.show), #takes us to a specific user's info
    url(r'^users/new$', views.new), #creates a new user
    url(r'^users/(?P<id>\d+)/edit$', views.edit ), #edits info for a specific user
    url(r'^users/create$', views.create), #deletes info for a specific user
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^users/(?P<id>\d+)/update$', views.update),
]
