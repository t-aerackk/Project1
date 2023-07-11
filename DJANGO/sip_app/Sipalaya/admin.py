from django.contrib import admin
from .models import *

class EmployeeView(admin.ModelAdmin):
    list_display=['id','first_name', 'last_name','Address','Phone']

# Register your models here.
admin.site.register(EmployeeInfo, EmployeeView, ),
admin.site.register(ImageHandler),
