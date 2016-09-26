"""MiniappsFinanceBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
   # ex: /polls/play/33/size
    url(r'^(?P<size>[0-9]+)/size/$', views.play, name='play'),
    # ex: /polls/push/
    url(r'^push/$', views.push_test, name='push_test'),
    # ex: /polls/5/move/
    url(r'^(?P<button>[0-9]+)/move/$', views.move, name='move'),
    # ex: /polls/help/
    url(r'^help/$', views.help, name='help'),
    # ex: /polls/score/
    url(r'^score/$', views.score, name='score'),
    """


from django.conf.urls import url
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url
import views

urlpatterns = [
    # ex: /polls/
    # ex: /polls/
    #url(r'^polls/$', views.index, name='index'),
    # ex: /polls/play/33/size
    url(r'^polls/(?P<frome>[0-9]+)/(?P<to>[0-9]+)/$', views.play, name='play'),
    #url(r'^polls/$', views.play, name='play'),
    #url(r'^polls/dispButtons/$', views.index, name='dispButtons'),

    #url(r'^polls/(?P<num>[0-9]+)/$', views.displayPrice, name='displayPrice'),
]