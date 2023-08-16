from django.core.management.base import BaseCommand
from hw2.models import Product


class Command(BaseCommand):
    help = "Add 10 products to a database"

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(name=f'Product{i}',
                              description=f'Description{i}',
                              price=i,
                              quantity=i+1)
            product.save()
            self.stdout.write(f'{product}')