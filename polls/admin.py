from django.contrib import admin

from .models import Choice, Question

# Takes a lot of screen space to display all
# the fields for entering related Choice (stacked fields)
# class ChoiceInline(admin.StackedInline):

# a tabular way of displaying inline related objects
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)