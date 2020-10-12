from django.contrib import admin
from .models import User
from apps.data.models import Athlete, Coach,  Sport, Training

# Register your models here.

admin.site.register(User)
admin.site.register(Athlete)
admin.site.register(Coach)
admin.site.register(Sport)
admin.site.register(Training)