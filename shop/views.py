from django.shortcuts import render
from shop.models import Product,Order
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def dashboard(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    return render(request,'shop/dashboard.html',{'orders':orders,'products':products})
