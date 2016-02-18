from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse


def index(request):
    s = "Hello!<br/><a href=\"%s\">All photos</a>" % reverse('gallery:index')
    return HttpResponse(s)


def page(request, page_number):
    s = "This is page # %s</br>" % page_number
    s += "<a href='%s'>Next page</a>" % reverse('gallery:page', args=(int(page_number)+1,))
    return HttpResponse(s)
