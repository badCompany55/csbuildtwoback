from django.contrib import admin
from map.models import Map
from api.models import Message

# Register your models here.
admin.site.register(Map)
admin.site.register(Message)
