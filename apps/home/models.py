from django.db import models
from django.utils.translation import ugettext_lazy as _
from my_roga.models import ActivityTracking
from my_roga.managers import ActivityQuerySet


class Language(ActivityTracking):
    name = models.CharField(max_length=50, unique=True,
                help_text=_('Language name'), 
                verbose_name=_('Language name'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")
        ordering = ['-created_at']


class MyRogaCategory(ActivityTracking):
    name = models.CharField(max_length=56, unique=True,
                help_text=_('Category name'), 
                verbose_name=_('Category name'))
    description = models.TextField(blank=True, null=True, 
                help_text=_('Category Description'),
                verbose_name=_('Category Description'))

    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("MyRoga Category")
        verbose_name_plural = _("MyRoga Categories")
        ordering = ['-created_at']


class MarketPlace(ActivityTracking):
    name = models.CharField(max_length=56, unique=True,
                help_text=_('Market place name'), 
                verbose_name=_('Market place name'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Market Place")
        verbose_name_plural = _("Market Places")
        ordering = ['-created_at']


class MarketPlaceCategory(ActivityTracking):
    market_place = models.ForeignKey('home.MarketPlace',
                related_name='market_place',
                on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True,
                help_text=_('Category name'), 
                verbose_name=_('Category name'))
    description = models.TextField(blank=True, null=True, 
                help_text=_('Category Description'),
                verbose_name=_('Category Description'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Market Place Category")
        verbose_name_plural = _("Market Place Categories")
        ordering = ['-created_at']


class MyRogaMarketPlaceCategory(ActivityTracking):
    my_roga_category = models.ForeignKey('home.MyRogaCategory',
                related_name='my_roga_category',
                on_delete=models.CASCADE)
    market_place_category = models.ForeignKey('home.MarketPlaceCategory',
                related_name='market_place_category',
                on_delete=models.CASCADE)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return f"{self.my_roga_category.name} - {self.market_place_category.name}"

    class Meta:
        verbose_name = _("MyRoga and Market Place Category")
        verbose_name_plural = _("MyRoga and Market Place Categories")
        ordering = ['-created_at']


class LogModule(ActivityTracking):
    name = models.CharField(max_length=56, unique=True,
                help_text=_('Module name'), 
                verbose_name=_('Module name'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Log Module")
        verbose_name_plural = _("Log Module")
        ordering = ['-created_at']


class Logs(ActivityTracking):
    LOG_TYPES = (
        ('DEBUG', _('DEBUG')),
        ('INFO', _('INFO')),
        ('WARNING', _('WARNING')),
        ('ERROR', _('ERROR')),
    )

    log_module = models.ForeignKey('home.LogModule',
                related_name='log_module',
                on_delete=models.CASCADE)
    log_type = models.CharField(max_length=128,
                choices=LOG_TYPES,
                help_text=_('Log Type'),
                verbose_name=_('Log Type'),
                default='Error',
                null=True, blank=True)
    message = models.TextField(blank=True, null=True,
                help_text=_('Error Message'),
                verbose_name=_('Error Message'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return f"{self.log_module.name} - {self.log_type}"

    class Meta:
        verbose_name = _("Logs")
        verbose_name_plural = _("Logs")
        ordering = ['-created_at']