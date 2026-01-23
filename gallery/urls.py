from django.urls import path

from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('projects_gallery/', views.projects_gallery, name='projects')
]