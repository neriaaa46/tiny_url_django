from django.http import HttpResponse


def create(request):
    return HttpResponse("Hi Create")


def redirect_short(request):
    return HttpResponse("Hi Short")
