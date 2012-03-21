from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
	(None,	{'fields': ['question','poll_type']}),
	('Date info', {'fields': ['open_date','close_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question',)#, 'pub_date', 'was_published_today')
#    list_filter = ['pub_date']
    search_fields = ['question']
#    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
