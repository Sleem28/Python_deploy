from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Add 10 users to a database"

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client(name=f'Client{i}',
                            email=f'client{i}@mail.com',
                            phone=f'+37529653{i}',
                            address=f'City{i}')
            client.save()
            self.stdout.write(f'{client}')
