from django.contrib import admin
from .models import Hospital, MedicalStaff
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug':('hospital_name',)}

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(MedicalStaff)