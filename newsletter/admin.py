
from django.contrib import admin
from .models import User, Log, JobScheduler,Newsletter

admin.site.register(User)
admin.site.register(Log)
admin.site.register(JobScheduler)
admin.site.register(Newsletter)