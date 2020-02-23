from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    model = Person

admin.site.register(Person, PersonAdmin)
