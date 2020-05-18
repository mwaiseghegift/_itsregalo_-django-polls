from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "itsregalo hackerthon votes"
admin.site.site_title = "itsregalo votes"
admin.site.index_title = "wecome to the future"

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
                ('Date Information', {'fields': ['pub_date'],'classes':
                ['collapse']}), ]
    inlines = [ChoiceInline]

    #classes is how its going to behave

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)