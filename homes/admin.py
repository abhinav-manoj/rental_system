from django.contrib import admin
from.models import *


# Register your models here.
class MasterAdmin(admin.ModelAdmin):
    list_display = ['created_date','isactive','created_user']
    def save_model(self, request, obj, form, change):
        obj.created_user = request.user
        return super().save_model(request, obj, form, change)
    
class StateAdmin(MasterAdmin):
    list_display = ['State_name','isactive','created_date','created_user']
    exclude = ['created_user']

admin.site.register(State,StateAdmin)
