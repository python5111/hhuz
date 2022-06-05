from django.contrib import admin
from .models import *

# Register your models here.
# class JobAdmin(admin.ModelAdmin):
#     list_display= ('citiy','title','salary','experience','age','phone','decription')

# class ResumeAdmin(admin.ModelAdmin):
#     list_display= ('citiy','full_name','genders','salary','experience','birth_date','phone','decription')


admin.site.register(Job_creat)
admin.site.register(Resume)
admin.site.register(Blog)

