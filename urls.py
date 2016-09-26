from django.contrib import admin
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^polls/(?P<frome>[0-9]+)/(?P<to>[0-9]+)/$', views.play, name='play'),
]
