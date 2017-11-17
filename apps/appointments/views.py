# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'belt_exam/index.html')

def appointments(request):
	if id not in session:
		return redirect('/')