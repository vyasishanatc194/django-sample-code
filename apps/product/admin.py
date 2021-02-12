from django.contrib import admin
from product.models import AspectsMetaData, AspectValuesMetaData, \
    ProductCatalog, AggregationModelSet


class AspectsMetaDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_model_aspect', 'model_title_order', \
        'model_title_text_before_aspect', 'model_title_text_after_aspect', \
        'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


class AspectValuesMetaDataAdmin(admin.ModelAdmin):
    list_display = ['aspect_meta_data', 'value_name', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


class ProductCatalogAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'hero_offer_price', 'second_hero_offer_price', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


class AggregationModelSetAdmin(admin.ModelAdmin):
    list_display = ['my_roga_category', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


admin.site.register(AspectsMetaData, AspectsMetaDataAdmin)
admin.site.register(AspectValuesMetaData, AspectValuesMetaDataAdmin)
admin.site.register(ProductCatalog, ProductCatalogAdmin)
admin.site.register(AggregationModelSet, AggregationModelSetAdmin)
