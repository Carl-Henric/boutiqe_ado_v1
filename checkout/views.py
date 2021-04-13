from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IfhS0CQrgfFebWxwPaGbfzae4viqRmu7py0CuxhfWZ6NXAa0UhhCVUhqzQfoL6Ab7QWSrbcyATsfdry1RlVpegH000DzEZolf',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)
