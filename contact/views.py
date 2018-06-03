# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.mail import send_mail

from django.conf import settings
from .forms import contactForm
from .models import ContactInfo
import logging
import pdb, traceback

from django.conf import settings #读取setting配置

logger = logging.getLogger(__name__)

DEBUG_PDB =settings.DEBUG_PDB

def contact(request):
    if DEBUG_PDB:
        pdb.set_trace()

    title = '聯系我們'
    form = contactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        subject = 'Message from HenryLab.com'
        message = '%s %s' %(message,name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
        title = "Thanks!"
        contactinfo = ContactInfo.objects.create(name=name, message=message, email=emailFrom )

        confirm_message = "Thanks for the message. We will get right back to you"
        form = None

    context = {'title':title, 'form':form,  'confirm_message':confirm_message}
    templates = 'contact/contact.html'
    return render(request,templates,context)
