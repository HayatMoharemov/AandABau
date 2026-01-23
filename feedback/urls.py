from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.feedback, name='feedbacks'),
    path('feedback/add_feedback', views.add_feedback,name='add_feedback'),
    path('feedback/view_feedbacks', views.view_feedbacks, name='view_feedbacks'),
]