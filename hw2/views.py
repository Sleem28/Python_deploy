from django.shortcuts import render, get_object_or_404
import logging
from .models import Client, Order, Product
from datetime import datetime, timedelta
from .forms import ProductForm


logger = logging.getLogger(__name__)


def last_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    w_orders = Order.objects.filter(client=client,
                                    date_of_order__gte=datetime.now() - timedelta(days=10))
    m_orders = Order.objects.filter(client=client,
                                    date_of_order__gte=datetime.now() - timedelta(days=30))
    y_orders = Order.objects.filter(client=client,
                                    date_of_order__gte=datetime.now() - timedelta(days=365))
    context = {
        'client':client,
        'w_orders':w_orders,
        'm_orders':m_orders,
        'y_orders':y_orders,
    }
    return render(request, 'hw2/show_orders.html', context)

def order_info(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = order.products.all()
    
    return render(request, 'hw2/products_info.html', {'order': order, 'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Data error!!!'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']

            logger.info(f'Got: {name=} {description=} {price=} {quantity=}')

            product = Product(name=name,
                              description=description,
                              price=price,
                              quantity=quantity,
                              image=image)
            product.save()
            message = 'Product saved.'
    else:
        form = ProductForm()
        message = 'Fill this product form out.'
    return render(request, 'hw2/add_product.html', {'form': form, 'message': message})
            
