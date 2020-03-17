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

admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(SubjToDept)
