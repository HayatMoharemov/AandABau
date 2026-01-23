from django.urls import path

from ourteam import views

app_name = 'ourteam'

urlpatterns = [
    path('our-team/', views.our_team, name='our_team')
]