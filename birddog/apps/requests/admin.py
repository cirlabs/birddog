from django.contrib import admin

from .models import Event, Request


########## INLINES ##########
class EventInline(admin.TabularInline):
    model = Event


########## ADMINS ##########
class RequestAdmin(admin.ModelAdmin):
    inlines = [EventInline]


admin.site.register(Request, RequestAdmin)
admin.site.register(Event, admin.ModelAdmin)
