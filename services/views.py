from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def services_overview(request:HttpRequest) -> HttpResponse:
    return render(request, 'services/services-overview.html')
def facade_works(request: HttpRequest) -> HttpResponse:
    return render(request, 'services/facade-works.html')

def insulation(request: HttpRequest) -> HttpResponse:
    return render(request, 'services/insulation.html')

def plastering(request: HttpRequest) -> HttpResponse:
    return render(request, 'services/plastering.html')

def renovation(request: HttpRequest) -> HttpResponse:
    return render(request, 'services/renovation.html')

def roof_repairs(request: HttpRequest) -> HttpResponse:
    return render(request, 'services/roof-repairs.html')

def sewer_construction(request: HttpRequest) -> HttpResponse:
    return render(request, 'services/sewer-construction.html')