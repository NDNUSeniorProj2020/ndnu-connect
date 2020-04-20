from django.contrib import admin
from .models import Tutor
from .models import Student
from .models import Department
from .models import Subject
from .models import Schedule
from .models import SubjToDept


admin.site.site_header = "NDNU Connect: Admin Portal"
admin.site.index_title = "NDNU Connect: Admin Portal"
admin.site.site_title = "NDNU Connect: Admin"

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','major','standing','method',)
    list_filter = ('major','standing',)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_subjects', 'rating', 'num_of_ratings', )
    list_filter = ('rating', 'subject',)




admin.site.register(Tutor,TutorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(SubjToDept)
