from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Consultant)
admin.site.register(models.Benchlist)
admin.site.register(models.ProspectConsultant)
admin.site.register(models.Submission)
