from django.contrib import admin
# from django.urls import path
from django.conf.urls import url

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home),
    url(r'^contact', views.contact),
    url(r'^add_new', views.AddItemView.as_view()),
    url(r'^views', views.ListItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/$', views.DetailItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/edit/$', views.UpdateItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/delete/$', views.DeleteItemView.as_view()),


]
