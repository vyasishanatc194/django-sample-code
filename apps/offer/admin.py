from django.contrib import admin
from offer.models import OfferAspectsMetaData, OfferAspectValuesMetaData, Offer


class OfferAspectsMetaDataAdmin(admin.ModelAdmin):
    list_per_page = 10


class OfferAspectValuesMetaDataAdmin(admin.ModelAdmin):
    list_per_page = 10


class OfferAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(OfferAspectsMetaData, OfferAspectsMetaDataAdmin)
admin.site.register(OfferAspectValuesMetaData, OfferAspectValuesMetaDataAdmin)
admin.site.register(Offer, OfferAdmin)