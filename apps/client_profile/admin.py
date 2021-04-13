from django.contrib import admin

from apps.client_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'is_active']
    list_editable = ['is_active', ]
    list_filter = ['is_active', ]
