from django.contrib import admin
from .models import quiz
# Register your models here.
from import_export.admin import ImportExportModelAdmin
@admin.register(quiz)

class viewAdmin(ImportExportModelAdmin):
    pass
