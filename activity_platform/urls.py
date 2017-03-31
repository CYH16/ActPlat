from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.activity_list, name='activity_list'),
	url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
	url(r'^about', views.activity_about, name='activity_about'),
]