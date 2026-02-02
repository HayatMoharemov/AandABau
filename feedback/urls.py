from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('', views.view_feedbacks, name='feedbacks'),
    path('add_feedbacks/', views.add_feedback, name='add_feedback'),
    path('submitted_feedback/', views.submitted_feedback, name='submitted_feedback')
]