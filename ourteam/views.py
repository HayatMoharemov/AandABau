from django.db.models import Prefetch
from django.views.generic import ListView, DetailView

from ourteam.models import TeamMembersModel


# Create your views here.

class OurTeamListView(ListView):
    model = TeamMembersModel
    template_name = 'ourteam/our-team.html'
    context_object_name = 'team_members'

class TeamMemberDetails(DetailView):
    model = TeamMembersModel
    template_name = 'ourteam/details.html'
    context_object_name = 'member_details'