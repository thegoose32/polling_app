from django.contrib import admin

from .models import Question, Choice, Company, User

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class UserAdmin(admin.TabularInline):
    model = User

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_start_year', 'company_size')
    inlines = [UserAdmin]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Company, CompanyAdmin)
