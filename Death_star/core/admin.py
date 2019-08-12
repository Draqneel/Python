from django.contrib import admin
from core.models import *

admin.site.site_header = 'Тренировочный лагерь Руки Тьмы'
admin.site.register(Planet)
admin.site.register(ShadowHandQuestion)
admin.site.register(QuestionChoice)


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Sith)
class SithAdmin(admin.ModelAdmin):
    autocomplete_fields = ('padavans',)
    search_fields = ('padavans__name',)
