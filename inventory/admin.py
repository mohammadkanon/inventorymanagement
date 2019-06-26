from django.contrib import admin
from inventory.models import Laptop, Desktop, Mobile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Laptop, Desktop, Mobile)

class ViewAdmin(ImportExportModelAdmin):
	pass