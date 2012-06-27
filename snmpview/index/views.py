# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from snmpview.index.models import Alist

def index(request, row_per_page=100):
    all_alarms = Alist.objects.using('alist').all()
    paginator = Paginator(all_alarms, int(row_per_page))
    page = request.GET.get('page')
    try:
        alarms = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        alarms = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        alarms = paginator.page(paginator.num_pages)
    return render_to_response('index.html',{'alarms': alarms, 'galarms': group(alarms)})

"""
internal helper function
returns iterator and append None as last element
(for function group(l) which ignore last element in the tuple)
input: [1,1,2,3,4,5,5,5]
output: [(1,1),(1,2),(2,3),(3,4),(4,5),(5,5),(5,5)]
"""
def pairs(l):
	for i in range(0,len(l)):
		if i<len(l)-1:
		    yield (l[i],l[i+1])
		else: yield (l[i], None)

"""
internal helper function
groups input array.
input: [1,2,3,3,3,4,5,5,5,5,5,6,7,7,7,8]
output: [[1], [2], [3, 3, 3], [4], [5, 5, 5, 5, 5], [6], [7, 7, 7], [8]]
"""
def group(l):
    res = []
    gr = []
    for t in pairs(l):
        i,j = t		# i,j - Alist object
        if j is None or i.target!=j.target:  # avoid AttributeError: 'NoneType' object has no attribute 'target'
            if gr:
                gr.append(i)
                res.append(gr)
                gr=[]
            else: res.append([i])
        else:
            gr.append(i)
    return res
