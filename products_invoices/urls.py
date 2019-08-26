from django.urls import path

from .views import (

    create_customer,
    create_product,
    create_invoice,
    single_invoice_details,
    view_all_invoices,
)


app_name = 'products_invoices'


urlpatterns = [

    path('create_customer/', create_customer, name='create_customer'),

    path('create_product/', create_product, name='create_product'),

    path('create_invoice/', create_invoice, name='create_invoice'),

    path('single_invoice_details/<int:id>/', single_invoice_details, name='single_invoice_details'),

    path('view_all_invoices/', view_all_invoices, name='view_all_invoices'),

]


