from django.contrib import admin
from apps.users.models import UserProfile, Organization


class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Organization, OrganizationAdmin)