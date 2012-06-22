from django.contrib import admin
from apps.requests.models import Event, Request, Agency

########## INLINES ##########

class EventInline(admin.TabularInline):
    model = Event


########## ADMINS ##########

class RequestAdmin(admin.ModelAdmin):
    inlines = [EventInline,]
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Request, RequestAdmin)


class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)


class AgencyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Agency, AgencyAdmin)