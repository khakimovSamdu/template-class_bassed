from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
# Create your views here.

class SmartphoneViews(View):
    def get(request: HttpRequest, pk: int = None):
        return HttpResponse("Dastur ishlashni boshladi")
