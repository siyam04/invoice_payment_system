from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .models import Customer, Product, Invoice
from .forms import CreateCustomerForm, CreateProductForm, CreateInvoiceForm

from custom_users.models import Profile


@login_required(login_url='login')
def create_customer(request):
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Customer Created Successfully!', extra_tags='safe')

            return redirect('home')
    else:
        form = CreateCustomerForm()

    template = 'products_invoices/create_customer.html'
    context = {'form': form}

    return render(request, template, context)


@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Product Created Successfully!', extra_tags='safe')

            return redirect('home')
    else:
        form = CreateProductForm()

    template = 'products_invoices/create_product.html'
    context = {'form': form}

    return render(request, template, context)


@login_required(login_url='login')
def create_invoice(request):
    if request.method == 'POST':
        form = CreateInvoiceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Invoice Created Successfully!', extra_tags='safe')

            return redirect('products_invoices:view_all_invoices')
    else:
        form = CreateInvoiceForm()

    template = 'products_invoices/create_invoice.html'
    context = {'form': form}

    return render(request, template, context)


@login_required(login_url='login')
def view_all_invoices(request, ):
    all_invoices = Invoice.objects.all()

    # Search
    query = request.GET.get('q')
    if query:
        all_invoices = all_invoices.filter(Q(item_code__icontains=query)).distinct()

    # Paginator
    paginator = Paginator(all_invoices, 4)
    page = request.GET.get('page')
    all_invoices_paginator_data = paginator.get_page(page)

    template = 'products_invoices/all_invoices.html'

    context = {
        'all_invoices': all_invoices,
        'all_invoices_paginator_data': all_invoices_paginator_data,
    }

    return render(request, template, context)


@login_required(login_url='login')
def single_invoice_details(request, id=None):

    invoice_details = Invoice.objects.get(id=id)
    # invoice_details_by_customer = Invoice.objects.get(customer__id=id)

    context = {
        # 'invoice_details_by_customer': invoice_details_by_customer,
        'invoice_details': invoice_details,
    }

    template = 'products_invoices/single_invoice_details.html'

    return render(request, template, context)

