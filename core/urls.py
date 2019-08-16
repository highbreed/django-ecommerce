from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import (
	ItemDetailView,
	CheckoutView,
	HomeView,
	OrderSummaryView,
	add_to_cart,
	remove_from_cart,
	remove_single_item_from_cart,
	PaymentView,
	AddCouponView,
	RequestRefundView,
	paypal_payments
)

app_name = 'core'

urlpatterns = [
	path('', views.home_view, name='home'),
	path('checkout/', CheckoutView.as_view(), name='checkout'),
	path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
	path('product/<slug>/', ItemDetailView.as_view(), name='product'),
	path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
	path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
	path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
	path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
		 name='remove-single-item-from-cart'),
	path('payment/<payment_option>/', PaymentView, name='payment'),
	url(r'^payments', paypal_payments, name='paypal-payments'),
	url(r'^paypal_return', views.paypal_return, name='paypal_return'),
	url(r'^paypal_cancel', views.paypal_cancel, name='paypal_cancel'),
	url(r'^paypal_url', include('paypal.standard.ipn.urls'), name='paypal-ipn'),
	url(r'^request-refund/', views.contact_view, name='request-refund'),
	url(r'^category/(?P<slug>[\w-]+)/$', views.show_category, name='category'),
	url(r'^refund_policy/$', views.return_policy, name='return-policy'),
	url(r'^terms_and_conditions/$', views.terms_and_conditions, name='terms_conditions'),
	url(r'^results/$', views.search, name='search'),

]
