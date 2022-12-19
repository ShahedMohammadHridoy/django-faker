from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth','gender','enrollment_date','email','phone_number','address')

admin.site.register(Student, StudentAdmin)
