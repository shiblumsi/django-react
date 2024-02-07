from django.contrib import admin
from .models import Person


# Register your models here.


class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['uid', 'name', 'email', 'phone_number', 'date_of_birth', 'gender', 'is_married', 'address', 'photo']


admin.site.register(Person, PersonModelAdmin)
