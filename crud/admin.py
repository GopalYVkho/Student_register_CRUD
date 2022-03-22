from django.contrib import admin
from crud.models import Student
# Register your models here.


class Student_Admin(admin.ModelAdmin):
    list=['sno','sname','sclass','saddress']

admin.site.register(Student,Student_Admin)
