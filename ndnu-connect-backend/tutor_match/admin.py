from django.contrib import admin

from .models import Tutor
from .models import Student
from .models import Department
from .models import Subject
from .models import Schedule
from .models import SubjToDept
from .models import TuitionLocation
from .models import TuitionMethod

# Register your models here.
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(SubjToDept)
admin.site.register(TuitionLocation)
admin.site.register(TuitionMethod)
