from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','std_name', 'std_address', 'email']

admin.site.register(Student, StudentAdmin)
