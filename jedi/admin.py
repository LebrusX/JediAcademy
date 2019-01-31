from django.contrib import admin
from jedi.models import Candidate, Jedi, Planet, Test

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class JediAdmin(admin.ModelAdmin):
    list_display = ('name', 'edu_planet')
    search_fields = ('name',)

class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TestAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'question1', 'question2', 'question3')


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Jedi, JediAdmin)
admin.site.register(Planet, PlanetAdmin)
admin.site.register(Test, TestAdmin)
