from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
def all_members(request):
  mymembers = Member.objets.all().values()
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(mymembers.render(context, request))