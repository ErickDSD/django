from django.conf.urls import include, url

from apps.iuafhome.views import index

urlpatterns = [
    url(r'^$', index),
]