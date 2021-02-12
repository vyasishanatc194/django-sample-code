from django.contrib import admin
from home.models import Language, MyRogaCategory, MarketPlace, \
    MarketPlaceCategory, MyRogaMarketPlaceCategory, LogModule, \
    Logs

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


class MyRogaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


class MarketPlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


class MarketPlaceCategoryAdmin(admin.ModelAdmin):
    list_per_page = 10


class MyRogaMarketPlaceCategoryAdmin(admin.ModelAdmin):
    list_per_page = 10


class LogModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


class LogsAdmin(admin.ModelAdmin):
    list_display = ['log_module', 'log_type', 'active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']
    list_per_page = 10


admin.site.register(Language, LanguageAdmin)
admin.site.register(MyRogaCategory, MyRogaCategoryAdmin)
admin.site.register(MarketPlace, MarketPlaceAdmin)
admin.site.register(MarketPlaceCategory, MarketPlaceCategoryAdmin)
admin.site.register(MyRogaMarketPlaceCategory, MyRogaMarketPlaceCategoryAdmin)
admin.site.register(LogModule, LogModuleAdmin)
admin.site.register(Logs, LogsAdmin)

