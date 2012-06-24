from django.contrib import admin

from .models import Agency


admin.site.register(Agency, admin.ModelAdmin)
