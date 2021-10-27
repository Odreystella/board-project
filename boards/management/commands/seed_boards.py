import random
from django.core.management import BaseCommand
from django_seed import Seed
from boards.models import Board
from users.models import User


class Command(BaseCommand):

    help = "This command creates many articles"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=10,
            type=int,
            help="How many articles do you want to creat?",
        )
    
    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        users = User.objects.all()
        seeder.add_entity(
            Board, 
            total, 
            {
                "writer" : lambda x: random.choice(users),
                "content" : lambda x: seeder.faker.sentence(),

            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} articles created!"))

