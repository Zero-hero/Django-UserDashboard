from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^logout/', views.logout, name="logout"),
	url(r'^new/', views.new, name="new"),
	url(r'^add_new/', views.add_new, name="add_new"),
	url(r'^my_profile/(?P<user_id>\d+)/$', views.my_profile, name="my_profile"),
	url(r'^update_profile/(?P<user_id>\d+)/$', views.update_profile, name="update_profile"),
	url(r'^update_profile_pw/(?P<user_id>\d+)/$', views.update_profile_pw, name="update_profile_pw"),
	url(r'^update_profile_desc/(?P<user_id>\d+)/$', views.update_profile_desc, name="update_profile_desc"),
	url(r'^admin_edit/(?P<user_id>\d+)/$', views.admin_edit, name="admin_edit"),

]