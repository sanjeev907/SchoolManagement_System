from django.contrib import admin
from .models import *
# Register your models here.

class schoolAdmin(admin.ModelAdmin):
    list_display=['email','name','city','pincode','password']

admin.site.register(school,schoolAdmin)

class studentsAdmin(admin.ModelAdmin):
    list_display=['school_name','name','grade','username','password']

admin.site.register(students,studentsAdmin)