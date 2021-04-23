from django.contrib import admin
from testapp.models import Matche

# Register your models here.
class MatcheAdmin(admin.ModelAdmin):
    list_display = ['mdate','mmatch','mtime','mvenue','mmypred',]

admin.site.register(Matche,MatcheAdmin)
