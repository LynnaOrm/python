from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
from time import strftime
# Create your models here.

class appointments(models.Model):
	date = models.DateField()
	time = models.TimeField()
	tasks = models.CharField(max_length=100)
	status = models.CharField(max_length=45)
	user = models.ForeignKey('belt_exam.User', related_name="usersappts")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = models.Manager()