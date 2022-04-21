from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   data={
      'title':'Home'
   }
   return render(request,"index.html",data)


def feedback(request):
   data={
      'title':'feedback'
   }
   return render(request,"feedback.html",data)


def contact(request):
   data={
      'title':'contact'
   }
   return render(request,"contact.html",data)


def services(request):
   data={
      'title':'Home'
   }
   return render(request,"services.html",data)



def about(request):
   data={
      'title':'Home'
   }
   return render(request,"about.html",data)

