from django.contrib import admin
from .models import Docteur, Patient, Rv

# Register your models here.
admin.site.register(Docteur)
admin.site.register(Patient)
admin.site.register(Rv)