from django.contrib import admin

from ourteam.models import TeamMembersModel


@admin.register(TeamMembersModel)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','position','date_joined']