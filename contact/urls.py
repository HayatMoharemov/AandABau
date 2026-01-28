from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.contacts,name='contact'),
    path('submitted-request', views.submitted_request ,name='submitted-request')
]