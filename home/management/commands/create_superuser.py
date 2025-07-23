from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create a superuser for production deployment'

    def handle(self, *args, **options):
        # Only create superuser if none exists and we're in production
        if not User.objects.filter(is_superuser=True).exists():
            username = os.environ.get('SUPERUSER_USERNAME', 'portfolio')
            email = os.environ.get('SUPERUSER_EMAIL', 'victorjosh4me@gmail.com')
            password = os.environ.get('SUPERUSER_PASSWORD', 'portfolio')
            
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created superuser: {username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Superuser already exists, skipping creation.')
            )
