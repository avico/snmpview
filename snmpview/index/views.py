# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from snmpview.index.models import Alist

def index(request):
	alarms = Alist.objects.using('alist')[:50]
        return render_to_response('index.html',{'alarms': alarms})
