from django.contrib import admin

# Register your models here.
from .models import IPOInfo

@admin.register(IPOInfo)
class IPOInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'price_band', 'ipo_price', 'listing_price', 'status')
