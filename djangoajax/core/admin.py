from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_displayed = ('id', 'name', 'course')

admin.site.register(Student, StudentAdmin)
