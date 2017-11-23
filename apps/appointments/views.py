# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..belt_exam.models import User #import the folder and class
from .models import *
from datetime import date

# Create your views here.
def index(request):
	return render(request, 'belt_exam/index.html')

def show_appt(request):
	print "****"
	if 'user_id' not in request.session:
		return redirect('/')
	try:
		#print 'setting up context'
		context = {
		'user': User.objects.get(id=request.session['user_id']),
		'appts': appointments.objects.filter(user=User.objects.get(id=request.session['user_id'])).exclude(date__lte=datetime.now(),time__gte=datetime.now()),
		# 'appts': appointments.objects.filter(user=User.objects.get(id=request.session['user_id']), date__gt=datetime.now()),
		'todays_appts': appointments.objects.filter(date=datetime.now(),time__gte=datetime.now(), user=User.objects.get(id=request.session['user_id'])),
		'other_appts': appointments.objects.all().exclude(user_id=request.session['user_id']),
		'join_appts': appointments.objects.filter(users_joining=User.objects.get(id=request.session['user_id']))
		
		}
		return render(request, 'appointments/appointments.html', context)
	except:
		print 'didnt set up context'
		return render(request, 'appointments/appointments.html')
	#return render(request, 'appointments/appointments.html')

def edit_appt(request, id):
	context = {
		'appt': appointments.objects.get(id=id)
	}
	return render(request, 'appointments/update.html', context)


def update_appt(request, id):
	if request.method == 'POST':
		updated_appt = appointments.objects.update(id, request.POST)
		if updated_appt[0] == False:
			for error in updated_appt[1]:
				messages.add_message(request, messages.INFO, error)
				return redirect(reverse('edit_appt', kwargs={'id':id}))
		else:
			return redirect('/appointments')

def add_appt(request):
	print request.POST
	new_appt = appointments.objects.make(request.POST)
	if new_appt[0] == False:
		for error in new_appt[1]:
			messages.add_message(request, messages.INFO, error)
			return redirect('/appointments')
	else:
		appointments.objects.create(date=request.POST['date'], time=request.POST['time'], tasks=request.POST['tasks'], status="pending", user=User.objects.get(id=request.session['user_id']))
		return redirect('/appointments')


def delete_appt(request, id):
	appt = appointments.objects.get(id=id)
	appt.delete()
	return redirect('/appointments')

def join(request, id):
	user = User.objects.get(id=request.session['user_id'])
	apps = appointments.objects.get(id=id)
	user.appointments_joined.add(apps)
	return redirect('/appointments')