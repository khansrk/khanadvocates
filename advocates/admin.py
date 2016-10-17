from django.contrib import admin
from advocates.models import *

# Register your models here.

admin.site.register(Track)
admin.site.register(Court)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('clientname', 'status', 'track','court','hearing_date',)
    search_fields = ['clientname', 'status']
    actions = ['make_approved',]

    def make_approved(self, request, queryset):
        rows_updated = queryset.update(status = 'a')
        if rows_updated == 1:
            message_bit = '1 session was'
        else:
            message_bit = '%s sessions were' % rows_updated

        self.message_user(request, '%s approved.' % message_bit)
    make_approved.short_description = 'Mark session(s) as approved'

admin.site.register(Session, SessionAdmin)

