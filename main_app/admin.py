from django.contrib import admin
from .models import Digimon, Playtime, Pet

# Register your models here.
admin.site.register(Digimon)
# before a Model can be CRUD'd using the built in Django admin portal, it must be registered
admin.site.register(Playtime)
admin.site.register(Pet)