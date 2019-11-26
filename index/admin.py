from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Password', 'Buyer_Email', 'Server')
    ordering = ('Username',)
    search_fields = ( 'Buyer_Email', 'Username', 'Server')
