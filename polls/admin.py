from django.contrib import admin
from .models import choice, Question

class ChoiceInline(admin.StackedInline):
    model = choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)