from django.contrib import admin

from .models import Team, HomePage, Cause, Work, About


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    prepopulated_fields = {'slug': ('fullname',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


class CauseInlineAdmin(admin.StackedInline):
    model = Cause
    extra = 1


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = [CauseInlineAdmin]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass
