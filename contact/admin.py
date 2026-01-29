from django.contrib import admin

from contact.models import ContactForm


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'submitted_at']