from django.db import models
from django.utils.translation import ugettext_lazy as _
from my_roga.models import ActivityTracking
from my_roga.managers import ActivityQuerySet


class AspectsMetaData(ActivityTracking):
    ASPECT_TYPE = (
        ('1', _('Closed')),
        ('2', _('Open')),
    )

    ASPECT_INPUT_TYPE = (
        ('1', _('Single')),
        ('2', _('Multi')),
    )

    my_roga_category = models.ForeignKey('home.MyRogaCategory',
                related_name='aspect_meta_data_my_roga_category',
                on_delete=models.CASCADE)
    name = models.CharField(max_length=255,
                help_text=_('Aspect name'), 
                verbose_name=_('Aspect name'))
    aspect_type = models.CharField(max_length=128,
                choices=ASPECT_TYPE,
                help_text=_('Aspect meta data type'),
                verbose_name=_('Aspect meta data type'),
                null=True, blank=True)
    aspect_input_type = models.CharField(max_length=128,
                choices=ASPECT_INPUT_TYPE,
                help_text=_('Aspect meta data input type'),
                verbose_name=_('Aspect meta data input type'),
                null=True, blank=True)
    is_model_aspect = models.BooleanField(default=False,
                verbose_name=_('Is Model Aspect?'),
                help_text=_('Is Model Aspect?'),)
    model_title_order = models.IntegerField(default=None,
                null=True, blank=True,
                help_text=_('Model Title Order'), 
                verbose_name=_('Model Title Order'))
    model_title_text_before_aspect = models.CharField(max_length=255,
                null=True, blank=True,
                help_text=_('Model Title Text Before Aspect'), 
                verbose_name=_('Model Title Text Before Aspect'))
    model_title_text_after_aspect = models.CharField(max_length=255,
                null=True, blank=True,
                help_text=_('Model Title Text After Aspect'), 
                verbose_name=_('Model Title Text After Aspect'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Aspects Meta Data")
        verbose_name_plural = _("Aspects Meta Data")
        ordering = ['-created_at']


class AspectValuesMetaData(ActivityTracking):
    VALUE_TYPE = (
        ('1', _('Text')),
        ('2', _('Number')),
    )

    aspect_meta_data = models.ForeignKey('product.AspectsMetaData',
                related_name='aspect_values_meta_data',
                on_delete=models.CASCADE)
    my_roga_category = models.ForeignKey('home.MyRogaCategory',
                related_name='aspect_values_my_roga_category',
                on_delete=models.CASCADE)
    value_name = models.CharField(max_length=255,
                help_text=_('Value Name'),
                verbose_name=_('Value Name'))
    normalized_aspect_value = models.CharField(max_length=255,
                help_text=_('Normalized Aspect Value'),
                verbose_name=_('Normalized Aspect Value'),
                null=True, blank=True)
    value_type = models.CharField(max_length=128,
                choices=VALUE_TYPE,
                help_text=_('Value type'),
                verbose_name=_('Value type'),
                null=True, blank=True)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.value_name

    class Meta:
        verbose_name = _("Aspect Values Meta Data")
        verbose_name_plural = _("Aspect Values Meta Data")
        ordering = ['-created_at']


class ProductCatalog(ActivityTracking):
    PRODUCT_STATUS = (
        ('1', _('Live')),
        ('2', _('Deleted')),
    )

    my_roga_category = models.ForeignKey('home.MyRogaCategory',
                related_name='product_my_roga_category',
                null=True,
                on_delete=models.SET_NULL)
    language = models.ForeignKey('home.Language',
                related_name='product_language',
                null=True,
                on_delete=models.SET_NULL)
    
    # For Now this two columns hero_offer and second_offer not in use
    hero_offer = models.ForeignKey('offer.Offer',
                related_name='product_hero_offer',
                null=True,
                on_delete=models.SET_NULL)
    second_offer = models.ForeignKey('offer.Offer',
                related_name='product_second_offer',
                null=True,
                on_delete=models.SET_NULL)
    title = models.CharField(max_length=255,
                help_text=_('Product title'), 
                verbose_name=_('Product title'),
                blank=True, null=True)
    description = models.TextField(blank=True, null=True,
                help_text=_('Product Description'),
                verbose_name=_('Product Description'))
    product_status = models.CharField(max_length=128,
                choices=PRODUCT_STATUS,
                help_text=_('Product Status'),
                verbose_name=_('Product Status'),
                null=True, blank=True)
    product_stealth = models.CharField(max_length=50,
                null=True, blank=True,
                help_text=_('Product Stealth'),
                verbose_name=_('Product Stealth'))
    technical_aspects = models.ManyToManyField('product.AspectsMetaData',
                related_name='product_technical_aspects')
    technical_aspect_values = models.ManyToManyField('product.AspectValuesMetaData',
                related_name='product_technical_aspect_values')
    
    # New Columns
    image_url = models.TextField(blank=True, null=True,
                help_text=_('Product Image URL'),
                verbose_name=_('Product Image URL'))
    review_url = models.TextField(blank=True, null=True,
                help_text=_('Review URL'),
                verbose_name=_('Review URL'))
    review_count = models.IntegerField(null=True, blank=True, default=0,
                help_text=_('Review Count'), 
                verbose_name=_('Review Count'))
    review_score = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Review Score'),
                verbose_name=_('Review Score'))
    hero_offer_url = models.TextField(blank=True, null=True,
                help_text=_('Hero Offer URL'),
                verbose_name=_('Hero Offer URL'))
    hero_offer_price = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Hero Offer Price'),
                verbose_name=_('Hero Offer Price'))
    hero_offer_market_place = models.ForeignKey('home.MarketPlace',
                related_name='hero_offer_market_place',
                null=True,
                on_delete=models.SET_NULL)
    second_hero_offer_url = models.TextField(blank=True, null=True,
                help_text=_('Second Hero Offer URL'),
                verbose_name=_('Second Hero Offer URL'))
    second_hero_offer_price = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Second Hero Offer Price'),
                verbose_name=_('Second Hero Offer Price'))
    second_hero_offer_market_place = models.ForeignKey('home.MarketPlace',
                related_name='second_hero_offer_market_place',
                null=True,
                on_delete=models.SET_NULL)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product Catalog")
        verbose_name_plural = _("Product Catalog")
        ordering = ['-created_at']


class AggregationModelSet(ActivityTracking):
    my_roga_category = models.ForeignKey('home.MyRogaCategory',
                related_name='aggregation_my_roga_category',
                null=True,
                on_delete=models.SET_NULL)
    aspects = models.ManyToManyField('product.AspectsMetaData',
                related_name='aggregation_technical_aspects')
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return f"{self.my_roga_category.name}"

    class Meta:
        verbose_name = _("Aggregation Model Set")
        verbose_name_plural = _("Aggregation Model Sets")
        ordering = ['-created_at']
