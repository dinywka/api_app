from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("OK")

def api(request):
    return JsonResponse(data = {"name": "DRF"}, safe = False)