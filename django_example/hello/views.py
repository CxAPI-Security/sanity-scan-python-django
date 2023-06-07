# Create your views here.
from django.http import HttpResponse


# Custom
def index(request):
    return HttpResponse("Hello (GET from `/hello`)")


# Custom
def param(request, param):
    return HttpResponse(f"Hello (GET from `/hello/:param ({param})`)")
