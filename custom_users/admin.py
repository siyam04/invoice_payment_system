from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'profile_name', 'address', 'image']
    list_display_links = ['user']
    list_filter = ['user']
    search_fields = ['user', 'address']


admin.site.register(Profile, ProfileAdmin)

