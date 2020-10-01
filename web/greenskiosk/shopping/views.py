from django.shortcuts import render
from catalogue.models import Product
from .models import Order
# Create your views here.

def add-to-cart(request):# use underscores, cartid and product id
    products = Product.objects.all()
    total_products = products.count()

    orders = Order.objects.all()
    total_orders = orders.count()

    context = {'orders': orders, 'total_orders': total_orders}
    return render(request, 'shopping/cart_items.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print("Printing POST:", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_items')


    context = {"form":form}
    return render(request, 'shopping/order_form.html', context)
    # customers = Customer.objects.all()
    
    # total_customers = customers.count()

    # total_orders = orders.count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()


    # context = {'orders': orders, 'customers': customers,
    # 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    # return render(request, 'accounts/dashboard.html', context)