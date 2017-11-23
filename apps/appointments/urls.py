#Appointment URLs
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.show_appt, name="show_appt"),
    # url(r'^appointments$', views.show_appt, name="show_appt"),
    url(r'^add_appt$', views.add_appt, name="add_appt"),
    url(r'^edit_appt/(?P<id>\d+)$', views.edit_appt, name="edit_appt"),
    url(r'^update_appt/(?P<id>\d+)$', views.update_appt, name="update_appt"),
    url(r'^delete_appt/(?P<id>\d+)$', views.delete_appt, name="delete_appt"),
    url(r'^join/(?P<id>\d+)$', views.join)
]