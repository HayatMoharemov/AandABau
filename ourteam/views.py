from django.core import paginator
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

from ourteam.models import TeamMembersModel


class OurTeamRolesView(TemplateView):
    model = TeamMembersModel
    template_name = 'ourteam/our-team.html'

class MemberDetailView(DetailView):
    model = TeamMembersModel
    context_object_name = 'member_details'
    template_name = 'ourteam/details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

def site_supervisor(request: HttpRequest) -> HttpResponse:
    members = TeamMembersModel.objects.filter(position='site_supervisor')

    paginator = Paginator(members, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'members': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'ourteam/site-supervisor.html', context)

def technical_manager(request: HttpRequest) -> HttpResponse:
    members = TeamMembersModel.objects.filter(position='technical_manager')

    paginator = Paginator(members, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'members': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'ourteam/technical-manager.html', context)

def construction_worker(request: HttpRequest) -> HttpResponse:
    members = TeamMembersModel.objects.filter(position='construction_worker')

    paginator = Paginator(members, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'members':page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'ourteam/construction-worker.html', context)

def office_administrator(request: HttpRequest) -> HttpResponse:
    members = TeamMembersModel.objects.filter(position='office_administrator')

    paginator = Paginator(members, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'members': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'ourteam/office-administrator.html', context)
