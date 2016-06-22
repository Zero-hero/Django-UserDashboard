from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^logout/', views.logout, name="logout"),
	url(r'^new/', views.new, name="new"),
	url(r'^add_new/', views.add_new, name="add_new"),
	url(r'^my_profile/(?P<user_id>\d+)/$', views.my_profile, name="my_profile"),
]