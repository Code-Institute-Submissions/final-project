from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils import timezone
from products.models import Product
from cart.models import OrderLineItem
from .forms import AddressForm
from .models import Address, Order
import stripe
import uuid

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET
@login_required(login_url='/accounts/login/')
def checkout(request):

	# Checkout view
	form = AddressForm()
	order_qs = Order.objects.filter(user= request.user, ordered=False)
	order_items = order_qs[0].orderitems.all()
	order_total = order_qs[0].get_totals() 
	context = {"form": form, "order_items": order_items, "order_total": order_total }
	# Getting the saved saved_address
	saved_address = Address.objects.filter(user = request.user)
	if saved_address.exists():
		savedAddress = saved_address.first()
		context = {"form": form, "order_items": order_items, "order_total": order_total, "savedAddress": savedAddress}
	if request.method == "POST":
		saved_address = Address.objects.filter(user = request.user)
		if saved_address.exists():
			savedAddress = saved_address.first()
			form = AddressForm(request.POST, instance=savedAddress)
			if form.is_valid():
				billingaddress = form.save(commit=False)
				billingaddress.user = request.user
				billingaddress.save()
				return redirect(reverse('payment'))
		else:
			form = AddressForm(request.POST)
			if form.is_valid():
				billingaddress = form.save(commit=False)
				billingaddress.user = request.user
				billingaddress.save()
				return redirect(reverse('payment'))
	
	return render(request, 'checkout.html', context)

@login_required(login_url='/accounts/login/')	
def payment(request):
	key = settings.STRIPE_PUBLISHABLE
	order_qs = Order.objects.filter(user= request.user, ordered=False)
	order_total = order_qs[0].get_totals() 
	totalCents = float(order_total * 100);
	total = round(totalCents, 2)
	if request.method == 'POST':
		charge = stripe.Charge.create(amount=total,
            currency='eur',
            description=order_qs,
            source=request.POST['stripeToken'])
		print(charge)
        
	return render(request, 'payment.html', {"key": key, "total": total})



@login_required(login_url='/accounts/login/')
def charge(request):
	order = Order.objects.get(user=request.user, ordered=False)
	orderitems = order.orderitems.all()
	order_total = order.get_totals()
	totalCents = int(float(order_total * 100))
	saved_address = Address.objects.filter(user = request.user)
	savedAddress = saved_address.first()
	if request.method == 'POST':
		charge = stripe.Charge.create(amount=totalCents,
            currency='eur',
            description=order,
            source=request.POST['stripeToken'])
		print(charge)
		if charge.status == "succeeded":
			orderId = get_random_string(length=16, allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
			print(charge.id)
			order.ordered = True
			order.paymentId = charge.id
			order.orderId = f'#{request.user}{orderId}'
			order.address = savedAddress
			order.save()
			cartItems = OrderLineItem.objects.filter(user=request.user)
			for item in cartItems:
				item.purchased = True
				item.save()
				
			subject = 'Order Confirmation'
			message = 'Thank you for your order. We will be incontact with you shortly.', order.orderId
			from_email = settings.EMAIL_HOST_USER
			to_list = [request.user.email, settings.EMAIL_HOST_USER]
			send_mail (subject, message, from_email, to_list, fail_silently=True)

		return render(request, 'charge.html', {"items": orderitems, "order": order })


@login_required(login_url='/accounts/login/')
def order_view(request):

	try:
		orders = Order.objects.filter(user=request.user, ordered=True)
		context = {
			"orders": orders
		}
	except:
		messages.warning(request, "You do not have an active order")
		return redirect('/')
	return render(request, 'orders.html', context)