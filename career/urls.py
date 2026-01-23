from django.urls import path

from career import views

app_name = 'career'

urlpatterns = [
    path('available_jobs/', views.available_jobs,name='available-jobs'),
    path('available_jobs/site_supervisor/', views.site_supervisor, name='site_supervisor'),
    path('available_jobs/technical_manager/', views.technical_manager, name='technical_manager'),
    path('available_jobs/construction_worker/', views.construction_worker, name='construction_worker'),
    path('available_jobs/office_administrator/', views.office_administrator, name='office_administrator'),
]