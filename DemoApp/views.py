# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, CreateView, ListView
from demo1 import settings

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
class LoginUser(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'login.html', context=None)

def loginUser(request):
	if request.method == 'POST':
		if request.POST.get('id'):
			try:
				reg = Registration.objects.get(id=request.POST.get('id'))
				req.email = request.POST.get('email1')
				req.password = request.POST.get('password1')
			except Registration.DoesNotExist:
				pass
			return redirect('/login/')

