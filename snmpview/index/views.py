# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from snmpview.index.models import Alist

def index(request):
    all_alarms = Alist.objects.using('alist').all()
    paginator = Paginator(all_alarms, 50)
    page = request.GET.get('page')
    try:
        alarms = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        alarms = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        alarms = paginator.page(paginator.num_pages)
    return render_to_response('index.html',{'alarms': alarms})
