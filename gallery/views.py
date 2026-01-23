from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def projects_gallery(request: HttpRequest) -> HttpResponse:
    return render(request, 'gallery/projects_gallery.html')