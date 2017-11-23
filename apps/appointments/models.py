
from __future__ import unicode_literals
from ..belt_exam.models import User
from django.db import models
from datetime import datetime, date
from time import strftime
# Create your models here.
class AppointmentManager(models.Manager):
	def make(self, data):
		errors=[]
		# strftime defaults to today - don't need time
		if data['date'] == "" or data['date'] < strftime('%Y-%m-%d'):
			errors.append("Date must be current or future dated")
		if data['time'] == "":
			errors.append("Please enter time")
		if not len(data['tasks']) > 1:
			errors.append("Please enter task(s)")
		if data['date'] != "" and appointments.objects.filter(date=data['date']) and appointments.objects.filter(time=data['time']):
			errors.append("this appointment is overlaping another appointment(s)")
		if not errors:
			return(True, data)
		return(False, errors)
	def update(self, id, data):
		appt = appointments.objects.get(id=id)
		errors=[]
		if data['date'] == "" or data['date'] < strftime('%Y-%m-%d'):
				errors.append("Date must be current or future dated")
		if data['time'] == "":
			errors.append("Please enter time")
		if not len(data['tasks']) > 1:
			errors.append("Please enter task(s)")
		if errors:
			return(False, errors)
		else:
			appt.date = data['date']
			appt.time = data['time']
			appt.tasks = data['tasks']
			appt.status = data['status']
			#appt.user = data['user']
			appt.save()
			return(True, appointments)


class appointments(models.Model):
	date = models.DateField()
	time = models.TimeField()
	tasks = models.CharField(max_length=100)
	status = models.CharField(max_length=45)
	user = models.ForeignKey('belt_exam.User', related_name="usersappointments")
	users_joining = models.ManyToManyField(User, related_name="appointments_joined") #join tables
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = AppointmentManager()
    #def __repr__(self):
        #return "Appt: {} {} {}"