"""
wait for the database to be ready
"""
import time

from psycopg2 import OperationalError as PsycopError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, PsycopError):
                self.stdout.write('DB unavailable')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('DB available!'))
