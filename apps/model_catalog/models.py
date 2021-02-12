from django.db import models
from django.utils.translation import ugettext_lazy as _
from my_roga.models import ActivityTracking
from my_roga.managers import ActivityQuerySet


class ModelCatalog(ActivityTracking):
    MODEL_STATUS = (
        ('1', _('Live')),
        ('2', _('Deleted')),
    )

    product_catalog = models.ManyToManyField('product.ProductCatalog',
                related_name='model_catalog_products')
    aggregation_model_set= models.ForeignKey('product.AggregationModelSet',
                related_name='aggregation_model_catalog',
                on_delete=models.CASCADE)
    model_aggregation_key = models.TextField(help_text=_('Model Aggregation Key'),
                verbose_name=_('Model Aggregation Key'))
    my_roga_category = models.ForeignKey('home.MyRogaCategory',
                related_name='model_catalog_my_roga_category',
                null=True,
                on_delete=models.SET_NULL)
    language = models.ForeignKey('home.Language',
                related_name='model_catalog_language',
                null=True,
                on_delete=models.SET_NULL)

    # Not in Use until Offer Table Created
    hero_offer = models.ForeignKey('offer.Offer',
                related_name='model_catalog_hero_offer',
                null=True,
                on_delete=models.SET_NULL)
    second_offer = models.ForeignKey('offer.Offer',
                related_name='model_catalog_second_offer',
                null=True,
                on_delete=models.SET_NULL)

    # For now we will use this Product Catalog id for Hero Product
    # After that we will use the Offer Table id
    hero_product = models.ForeignKey('product.ProductCatalog',
                related_name='model_catalog_hero_product',
                null=True,
                on_delete=models.SET_NULL)
    hero_product_price = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Hero Product Price'),
                verbose_name=_('Hero Product Price'))
    hero_product_market_place = models.ForeignKey('home.MarketPlace',
                related_name='hero_product_market_place',
                null=True,
                on_delete=models.SET_NULL)
    second_hero_product = models.ForeignKey('product.ProductCatalog',
                related_name='model_catalog_second_hero_product',
                null=True,
                on_delete=models.SET_NULL)
    second_hero_product_price = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Second Hero Product Price'),
                verbose_name=_('Second Hero Product Price'))
    second_hero_product_market_place = models.ForeignKey('home.MarketPlace',
                related_name='second_hero_product_market_place',
                null=True,
                on_delete=models.SET_NULL)

    title = models.CharField(max_length=255,
                help_text=_('Model title'), 
                verbose_name=_('Model title'))
    description = models.TextField(blank=True, null=True,
                help_text=_('Model Description'),
                verbose_name=_('Model Description'))
    description_image_url = models.TextField(blank=True, null=True,
                help_text=_('Model Description Image URL'),
                verbose_name=_('Model Description Image URL'))
    model_status = models.CharField(max_length=128,
                choices=MODEL_STATUS,
                help_text=_('Model Status'),
                verbose_name=_('Model Status'),
                null=True, blank=True)
    model_stealth = models.CharField(max_length=50,
                null=True, blank=True,
                help_text=_('Model Stealth'),
                verbose_name=_('Model Stealth'))
    product_review_count = models.IntegerField(null=True, blank=True, default=0,
                help_text=_('Product Review Count'), 
                verbose_name=_('Product Review Count'))
    product_review_score = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Product Review Score'),
                verbose_name=_('Product Review Score'))
    image_url = models.TextField(blank=True, null=True,
                help_text=_('Model Image URL'),
                verbose_name=_('Model Image URL'))
    review_url = models.TextField(blank=True, null=True,
                help_text=_('Review URL'),
                verbose_name=_('Review URL'))
    recommendation_score = models.FloatField(max_length=11,
                null=True, blank=True, default=0,
                help_text=_('Recommendation Score'),
                verbose_name=_('Recommendation Score'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Model Catalog")
        verbose_name_plural = _("Model Catalog")
        ordering = ['-created_at']