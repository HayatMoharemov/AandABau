from gc import get_objects

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from career.forms import JobApplicationForm
from career.models import JobPositions, JobApplication


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

def available_job_positions_list(request: HttpRequest) -> HttpResponse:
    jobs = JobPositions.objects.all().order_by('-date_posted')
    paginator = Paginator(jobs, 4)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    total_pages = paginator.num_pages

    context = {
        'page': page,
        'total_pages': total_pages
    }

    return render(request, 'career/available-jobs-list.html', context)

def apply_for_job(request: HttpRequest, pk) -> HttpResponse:
    job = get_object_or_404(JobPositions, pk=pk)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('career:successful_application')
    else:
        form = JobApplicationForm(initial={'job_display': job.get_title_display()})

    context = {
        'form': form,
        'job': job
    }

    return render(request, 'career/apply_job.html', context)

def successful_application(request: HttpRequest) -> HttpResponse:
    return render(request, 'career/thanks-for-applying.html')