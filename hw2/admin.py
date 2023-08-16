from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
    ]

    fieldsets = [
        (
            'Client name',
            {
                "classes": ['wide'],
                "fields": ['name'],
            },
        ),
        (
            'Other client info',
            {
                'classes': ['collapse'],
                "description": 'Cathegories of the product.',
                'fields': ['email', 'phone', 'address']
            },
        ),
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'quantity',
    ]

    ordering = ['-price',]
    
    search_fields = ['description']
    search_help_text = 'Search by description.'


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'total_price',
        'date_of_order',
    ]

    ordering = ['client', 'date_of_order',]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
