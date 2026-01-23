from django.urls import path
from services import views

app_name = 'services'

urlpatterns = [
    path('services_overview', views.services_overview, name='services_overview'),
    path('services_overview/facade_works/', views.facade_works, name='facade_works'),
    path('services_overview/insulation/', views.insulation,name='insulation'),
    path('services_overview/plastering/', views.plastering, name='plastering'),
    path('services_overview/renovation/', views.renovation, name='renovation'),
    path('services_overview/roof_repairs/', views.roof_repairs, name='roof_repairs'),
    path('services_overview/sewer_construction/', views.sewer_construction, name='sewer_construction')
]