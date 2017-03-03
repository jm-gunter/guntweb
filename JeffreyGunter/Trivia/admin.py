from django.contrib import admin
from .models import Category, Game, Question, Round, Team, Venue

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Category, CategoryAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'venue', 'date']

admin.site.register(Game, GameAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text',]

admin.site.register(Question, QuestionAdmin)

class RoundAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Round, RoundAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Team, TeamAdmin)

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Venue, VenueAdmin)
