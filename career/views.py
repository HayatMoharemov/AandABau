from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def available_jobs(request: HttpRequest) -> HttpResponse:
    return render(request, 'career/available-jobs.html')
def site_supervisor(request: HttpRequest) -> HttpResponse:
    return render(request, 'career/site-supervisor.html')

def technical_manager(request: HttpRequest) -> HttpResponse:
    return render(request, 'career/technical-manager.html')

def construction_worker(request: HttpRequest) -> HttpResponse:
    return render(request, 'career/construction-worker.html')

def office_administrator(request: HttpRequest) -> HttpResponse:
    return render(request, 'career/office-administrator.html')