from django.contrib import admin
from friendsZones.models import User, Favorites, Block

# Register your models here.

admin.site.register(User)
admin.site.register(Favorites)
admin.site.register(Block)

