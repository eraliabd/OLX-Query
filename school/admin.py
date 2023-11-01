from django.contrib import admin

# Register your models here.
from .models import Region, District, School, Student, RegionMonthlyResult, Month

admin.site.register(Month)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(RegionMonthlyResult)
