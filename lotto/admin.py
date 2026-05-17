from django.contrib import admin
from .models import Ticket, Draw


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'numbers', 'mode', 'round_number', 'created_at')
    search_fields = ('name', 'numbers')
    list_filter = ('mode', 'round_number')


@admin.register(Draw)
class DrawAdmin(admin.ModelAdmin):
    list_display = ('id', 'round_number', 'winning_numbers', 'created_at')
    search_fields = ('winning_numbers',)