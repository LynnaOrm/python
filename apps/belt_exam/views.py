# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import date

# Create your views here.
def index(request):
    return render(request,'belt_exam/index.html')


# def appointments(request):
#     try:
#         request.session['user_id']
#     except KeyError:
#         return redirect('/')
#     context = {
#         'user': User.objects.get(id=request.session['user_id']),
#     }
#     return render(request, 'appointments/appointments.html', context)

def register(request):
    print request.POST
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Registered!")
    return redirect('/appointments')


def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Logged in!")
    today = date.today().strftime("%Y-%m-%d_%H:%M")
    return redirect('/appointments')

def logout(request):
    request.session.clear()
    return redirect('/')


