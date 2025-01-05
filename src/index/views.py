from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def showIndex(request):
    return render (request,"index.html")

def showtest(request):
   context ={
       "numbre": 10,
      "mesage" :"coucou mesage",
      "liste" :['tina','aina','fahazavana'],
      
   }
   return render (request,"test.html",context)