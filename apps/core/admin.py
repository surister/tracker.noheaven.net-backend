from django.contrib import admin

# Register your models here.
from apps.core.models import Tracker, Anime

admin.site.register([Tracker, Anime])
