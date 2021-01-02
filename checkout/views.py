from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I5FtgFIexVZCAP6oj5H88fIDJoLz4lTeRmBWvZ797XpJdasP3Y47me0rzszJaWSEsiVzMrkeNdla5AdFzTHL4Gb00PppqI44e',
    }

    return render(request, template, context)
