from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.activity_list, name='activity_list'),
    url(r'^activity_mine/$', views.activity_mine, name='activity_mine'),
	url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
	url(r'^about', views.activity_about, name='activity_about'),
	url(r'^accounts/login/$',views.login),
	url(r'^accounts/logout/$',views.logout),
	url(r'^accounts/register/$',views.register),
	url(r'^add_new/$',views.add_new),
]