from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def add_feedback(request: HttpRequest) -> HttpResponse:
    return render(request, 'feedback/add_feedback.html')

def view_feedbacks(request: HttpRequest) -> HttpResponse:
    return render(request, 'feedback/view_feedbacks.html')

def feedback(request: HttpRequest) -> HttpResponse:
    return render(request, 'feedback/feedback.html')