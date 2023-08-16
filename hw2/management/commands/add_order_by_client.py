from django.core.management.base import BaseCommand
from hw2.models import Client, Product, Order


class Command(BaseCommand):
    help = "Add an order by the client's id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self,*args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        order = Order(client=client)
        total_price = 0
        order.save()

        for i in range(1, 5):
            product = Product.objects.filter(pk=i).first()
            total_price += product.price
            order.products.add(product)
            order.save()

        order.total_price = total_price

        order.save()


