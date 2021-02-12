from django.contrib import admin
from model_catalog.models import ModelCatalog

# Register your models here.

class ModelCatalogAdmin(admin.ModelAdmin):
    list_display = ['title', 'model_aggregation_key', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at', 'delete_reason']
    list_per_page = 10


admin.site.register(ModelCatalog, ModelCatalogAdmin)