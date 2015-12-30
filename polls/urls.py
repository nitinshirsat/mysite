from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about_us', views.about_us),
    url(r'^', views.index, name='index'),
]