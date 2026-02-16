from django.urls import path

from ourteam import views
from ourteam.views import OurTeamRolesView, MemberDetailView, construction_worker, technical_manager, site_supervisor, \
    office_administrator

app_name = 'ourteam'

urlpatterns = [
    path('', OurTeamRolesView.as_view(), name='our_team'),
    path('construction_workers/', construction_worker,name='construction_worker'),
    path('technical_managers/', technical_manager,name='technical_manager'),
    path('site_supervisors/', site_supervisor ,name='site_supervisor'),
    path('office_administrators/', office_administrator,name='office_administrator'),
    path('<slug:slug>/', MemberDetailView.as_view(),name='member_details'),
]