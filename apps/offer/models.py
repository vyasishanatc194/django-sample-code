from django.db import models
from django.utils.translation import ugettext_lazy as _
from my_roga.models import ActivityTracking
from my_roga.managers import ActivityQuerySet


class OfferAspectsMetaData(ActivityTracking):
    ASPECT_TYPE = (
        ('1', _('Closed')),
        ('2', _('Open')),
    )

    ASPECT_INPUT_TYPE = (
        ('1', _('Single')),
        ('2', _('Multi')),
    )

    name = models.CharField(max_length=255,
                help_text=_('Offer Aspect name'), 
                verbose_name=_('Offer Aspect name'))
    aspect_type = models.CharField(max_length=128,
                choices=ASPECT_TYPE,
                help_text=_('Offer Aspect meta data type'),
                verbose_name=_('Offer Aspect meta data type'),
                null=True, blank=True)
    aspect_input_type = models.CharField(max_length=128,
                choices=ASPECT_INPUT_TYPE,
                help_text=_('Offer Aspect meta data input type'),
                verbose_name=_('Offer Aspect meta data input type'),
                null=True, blank=True)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Offer Aspects Meta Data")
        verbose_name_plural = _("Offer Aspects Meta Data")
        ordering = ['-created_at']


class OfferAspectValuesMetaData(ActivityTracking):
    VALUE_TYPE = (
        ('1', _('Text')),
        ('2', _('Number')),
    )

    aspect_meta_data = models.ForeignKey('offer.OfferAspectsMetaData',
                related_name='offer_aspect_values_meta_data',
                on_delete=models.CASCADE)
    value_name = models.CharField(max_length=255,
                help_text=_('Offer Value Name'),
                verbose_name=_('Offer Value Name'))
    value_type = models.CharField(max_length=128,
                choices=VALUE_TYPE,
                help_text=_('Offer Value type'),
                verbose_name=_('Offer Value type'),
                null=True, blank=True)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.value_name

    class Meta:
        verbose_name = _("Offer Aspect Values Meta Data")
        verbose_name_plural = _("Offer Aspect Values Meta Data")
        ordering = ['-created_at']


class Offer(ActivityTracking):
    QUALIFICATION_STATUS = (
        ('1', _('Qualified')),
        ('2', _('Rejected')),
        ('2', _('Pending')),
    )

    title = models.CharField(max_length=255,
                help_text=_('Offer title'), 
                verbose_name=_('Offer title'))
    seller_offer_id = models.CharField(max_length=255,
                help_text=_('Seller Offer Id'), 
                verbose_name=_('Seller Offer Id'))
    asin = models.CharField(max_length=255,
                help_text=_('ASIN'), 
                verbose_name=_('ASIN'))
    market_place = models.ForeignKey('home.MarketPlace',
                related_name='offer_market_place',
                on_delete=models.CASCADE)
    offer_url = models.TextField(blank=True, null=True,
                help_text=_('Offer URL'),
                verbose_name=_('Offer URL'))
    offer_price = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Offer Price'),
                verbose_name=_('Offer Price'))
    offer_quantity = models.IntegerField(null=True, blank=True, default=0,
                help_text=_('Offer Quantity'), 
                verbose_name=_('Offer Quantity'))
    offer_reviews_count = models.IntegerField(null=True, blank=True, default=0,
                help_text=_('Offer Reviews Count'), 
                verbose_name=_('Offer Reviews Count'))
    offer_reviews_score = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Offer Reviews Score'),
                verbose_name=_('Offer Reviews Score'))
    offer_image_url = models.TextField(blank=True, null=True,
                help_text=_('Offer Image URL'),
                verbose_name=_('Offer Image URL'))
    offer_language = models.ForeignKey('home.Language',
                related_name='offer_language',
                null=True,
                on_delete=models.SET_NULL)
    brand_name = models.CharField(max_length=56,
                help_text=_('Offer Brand Name'), 
                verbose_name=_('Offer Brand Name'))
    mpn = models.CharField(max_length=56,
                help_text=_('Manufacturur Part Number'), 
                verbose_name=_('Manufacturur Part Number'))
    offer_description = models.TextField(blank=True, null=True,
                help_text=_('Offer Description'),
                verbose_name=_('Offer Description'))
    technical_aspects = models.ManyToManyField('offer.OfferAspectsMetaData',
                related_name='offer_technical_aspects')
    technical_aspect_values = models.ManyToManyField('offer.OfferAspectValuesMetaData',
                related_name='offer_technical_aspect_values')
    qualification_status = models.CharField(max_length=128,
                choices=QUALIFICATION_STATUS,
                help_text=_('Qualification Status'),
                verbose_name=_('Qualification Status'),
                null=True, blank=True)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")
        ordering = ['-created_at']