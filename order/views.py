# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# Create your views here.


@require_http_methods(["GET", "POST"])
def index(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass

@require_http_methods(["GET", "POST"])	
def listing(request, page_size=25):
	pass
#    contact_list = Contacts.objects.all()
#    paginator = Paginator(contact_list, page_size) # Show 25 contacts per page
#
#    #page = request.GET.get('page')
#    try:
#        #contacts = paginator.page(page)
#   #except PageNotAnInteger:
#        ## If page is not an integer, deliver first page.
#        contacts = paginator.page(1)
#    #except EmptyPage:
#        ## If page is out of range (e.g. 9999), deliver last page of results.
#        contacts = paginator.page(paginator.num_pages)
##
#    #return render(request, 'list.html', {'contacts': contacts})
	
