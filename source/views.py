import json
import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from custom_users.models import Profile


# Stripe keys
stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
stripe_sec = settings.STRIPE_SECRET_KEY
stripe.api_key = stripe_sec


def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = ''

    template = 'home.html'
    context = {
        'profile': profile,

        # Stripe key
        'key': stripe_pub,
    }

    return render(request, template, context)


# Stripe checkout
def checkout(request):
    amount = 500

    customer = stripe.Customer.create(email=request.POST['stripeEmail'],
                                      source=request.POST['stripeToken'])

    charge = stripe.Charge.create(customer=customer.id, amount=amount, currency='USD',
                                  description='Sample Charge')
    print('status', charge)

    return JsonResponse(charge)


# class HomeView(TemplateView):
#     template_name = 'home.html'
