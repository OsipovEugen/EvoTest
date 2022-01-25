from django.contrib import admin
from .models import Person
class PersonAdmin(admin.ModelAdmin):
	list_display = ('email', )

admin.site.register(Person, PersonAdmin)
# Register your models here.
