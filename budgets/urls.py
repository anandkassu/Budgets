from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home),
    path('contact', views.contact),
    path('add_new', views.AddItemView.as_view()),
    path('view', views.ListItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/$', views.DetailItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/edit/$', views.UpdateItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/delete/$', views.DeleteItemView.as_view()),


]
