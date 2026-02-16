from django.urls import path

from ourteam import views
from ourteam.views import OurTeamListView, TeamMemberDetails

app_name = 'ourteam'

urlpatterns = [
    path('', OurTeamListView.as_view(), name='our_team'),
    path('<slug:slug>/', TeamMemberDetails.as_view(),name='member_details')
]