from django.contrib import admin
#from django.contrib.auth.models import Group
from .models import Tutor
from .models import Student
from .models import Department
from .models import Subject
from .models import Schedule
from .models import SubjToDept

# Register your models here.
admin.site.site_header = "NDNU Conect Admin Page" #title
#admin.site.unregister(Group) #not displaying the Group
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','major','standing','method',)
    list_filter = ('major','standing',)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'rating', 'num_of_ratings', )
    list_filter = ('rating', 'subject',)


admin.site.register(Tutor,TutorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(SubjToDept)

# chainging how the tutor looks
