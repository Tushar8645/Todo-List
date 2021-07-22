from django.contrib import admin
from main.models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ('item', 'completed', 'created', 'modified',)
    readonly_fields = ('created', 'modified',)


admin.site.register(List, ListAdmin)
