from django.contrib import admin
from .models import Task, Workout, Workout_list, Finance

admin.site.register(Task)
admin.site.register(Workout)
admin.site.register(Workout_list)
admin.site.register(Finance)

