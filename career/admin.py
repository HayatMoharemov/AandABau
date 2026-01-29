from django.contrib import admin
from django.contrib.admin import ModelAdmin

from career.models import JobPositions, JobApplication


# Register your models here.
@admin.register(JobPositions)
class JobPositionsAdmin(ModelAdmin):
    list_display = ['title', 'location', 'employment_type', 'date_posted']
    search_fields = ['title', 'location']
    ordering = ['-date_posted']

@admin.register(JobApplication)
class JobApplicationAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name','job', 'submitted_at','is_hired']
    list_filter = ['job__title', 'is_hired']
    search_fields = ['first_name', 'last_name']
    read_only_fields = ['first_name', 'last_name', 'job__title', 'submitted_at']
    fields = ['first_name', 'last_name', 'is_hired']