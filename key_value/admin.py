from django.contrib import admin
from key_value.models import Store
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    fields = ('key','value','created_at')

admin.site.register(Store,StoreAdmin)