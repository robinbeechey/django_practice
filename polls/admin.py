from django.contrib import admin

# Register your models here.
from .models import Question, Choice, User

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Question Owner', {'fields': ['user']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'user')
    list_filter = ['pub_date']
    search_fields = ['question_text']




admin.site.register(Question, QuestionAdmin)