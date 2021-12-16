from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Hospital)
admin.site.register(Department)

admin.site.register(Time)

admin.site.register(appointment)
admin.site.register(Medicine)
admin.site.register(contact)


