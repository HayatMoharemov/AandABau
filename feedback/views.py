from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from feedback.forms import CreateFeedbackForm
from feedback.models import CreateFeedback


# Create your views here.
def add_feedback(request: HttpRequest) -> HttpResponse:

    form = CreateFeedbackForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('feedback:submitted_feedback')

    context = {
        'form': form
    }

    return render(request, 'feedback/add_feedback.html', context)

def view_feedbacks(request: HttpRequest) -> HttpResponse:

    feedbacks = CreateFeedback.objects.all()
    paginator = Paginator(feedbacks, 5)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    total_pages = paginator.num_pages

    context = {
        'page': page,
        'total_pages': total_pages
    }

    return render(request, 'feedback/feedback.html', context)

def submitted_feedback(request: HttpRequest) -> HttpResponse:
    return render(request, 'feedback/thanks-for-the-feedback.html')