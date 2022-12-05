from django.contrib import admin
from .models import Programmers
from .models import Languages,Languagesbg
# Register your models here.

admin.site.register(Programmers),
admin.site.register(Languages),
admin.site.register(Languagesbg)