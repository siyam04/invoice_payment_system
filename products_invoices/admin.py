from django.contrib import admin

from .models import (

    Customer,
    Product,
    Invoice,
    # Order,
)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'address', 'email']
    list_display_links = ['customer_name']
    list_filter = ['customer_name', 'email']
    search_fields = ['email', 'customer_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'description']
    list_display_links = ['product_name']
    list_filter = ['product_name', 'category']
    search_fields = ['product_name', 'category']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'currency', 'date', 'item_code', 'item_description', 'quantity', 'unit_price',
                    'discount', 'total']

    list_display_links = ['item_code']
    list_filter = ['item_code', 'customer', 'item_description']
    search_fields = ['item_code']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)



