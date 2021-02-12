from django.db import models
from django.utils.translation import ugettext_lazy as _
from my_roga.models import ActivityTracking
from my_roga.managers import ActivityQuerySet


class Quiz(ActivityTracking):
    name = models.CharField(max_length=56, unique=True,
                help_text=_('Quiz name'), 
                verbose_name=_('Quiz name'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['-created_at']


class Question(ActivityTracking):
    QUESTION_TYPE = (
        ('1', _('Usage/Place Question?')),
        ('2', _('Type Question?')),
        ('3', _('Budget Question?')),
    )

    quiz = models.ForeignKey('quiz.Quiz',
                related_name='quiz',
                on_delete=models.CASCADE)
    my_roga_category = models.ForeignKey('home.MyRogaCategory',
                related_name='question_my_roga_category',
                on_delete=models.CASCADE)
    name = models.CharField(max_length=255,
                help_text=_('Quiz name'), 
                verbose_name=_('Quiz name'))
    description = models.CharField(max_length=300,
                help_text=_('Quiz description'), 
                verbose_name=_('Quiz description'))
    question_type = models.CharField(max_length=128,
                choices=QUESTION_TYPE,
                help_text=_('Question type'),
                verbose_name=_('Question type'),
                null=True, blank=True)
    order = models.IntegerField(help_text=_('Question order'), 
                verbose_name=_('Question order'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['-created_at']


class Answer(ActivityTracking):
    question = models.ForeignKey('quiz.Question',
                related_name='question',
                on_delete=models.CASCADE)
    name = models.CharField(max_length=255,
                help_text=_('Answer name'), 
                verbose_name=_('Answer name'))
    value = models.CharField(max_length=255,
                help_text=_('Answer value'), 
                verbose_name=_('Answer value'))
    short_description = models.CharField(max_length=150,
                help_text=_('Answer short description'), 
                verbose_name=_('Answer short description'))
    long_description = models.CharField(max_length=300,
                help_text=_('Answer long description'), 
                verbose_name=_('Answer long description'))
    order = models.IntegerField(help_text=_('Answer order'), 
                verbose_name=_('Answer order'))
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['-created_at']


class AnswerMetaData(ActivityTracking):
    META_DATA_VALUE_TYPE = (
        ('1', _('Not Required')),
        ('2', _('Min')),
        ('3', _('Max')),
    )

    answer = models.ForeignKey('quiz.Answer',
                related_name='answer_meta_data',
                on_delete=models.CASCADE)
    name = models.CharField(max_length=255,
                help_text=_('Answer meta data name'), 
                verbose_name=_('Answer meta data name'))
    value = models.CharField(max_length=255,
                help_text=_('Answer meta data value'), 
                verbose_name=_('Answer meta data value'))
    value_type = models.CharField(max_length=128,
                choices=META_DATA_VALUE_TYPE,
                help_text=_('Answer meta data value type'),
                verbose_name=_('Answer meta data value type'),
                null=True, blank=True)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Answer Meta Data")
        verbose_name_plural = _("Answer Meta Data")
        ordering = ['-created_at']


class AnswerModelMap(ActivityTracking):
    answer = models.ForeignKey('quiz.Answer',
                related_name='answer_model',
                on_delete=models.CASCADE)
    model_catalog = models.ForeignKey('model_catalog.ModelCatalog',
                related_name='market_place_category',
                on_delete=models.CASCADE)
    
    objects = ActivityQuerySet.as_manager()

    def __str__(self):
        return f"{self.answer.name} - {self.model_catalog.title}"

    class Meta:
        verbose_name = _("Answer Model Mapping")
        verbose_name_plural = _("Answer Model Mappings")
        ordering = ['-created_at']