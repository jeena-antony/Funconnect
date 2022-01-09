from django.contrib import admin

# Register your models here.
from .models import game, mark
from .models import question

admin.site.register(game)
admin.site.register(question)
admin.site.register(mark)