from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def our_team(request: HttpRequest) -> HttpResponse:
    return render(request, 'ourteam/our-team.html')