from django.contrib import admin
from quiz.models import Quiz, Question, Answer, AnswerMetaData, \
    AnswerModelMap


class QuizAdmin(admin.ModelAdmin):
    list_per_page = 10


class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 10


class AnswerAdmin(admin.ModelAdmin):
    list_per_page = 10


class AnswerMetaDataAdmin(admin.ModelAdmin):
    list_per_page = 10


class AnswerModelMapAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(AnswerMetaData, AnswerMetaDataAdmin)
admin.site.register(AnswerModelMap, AnswerModelMapAdmin)