from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as PSycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand) :

    def handle(self,*args,**options):
        self.stdout.write('Waiting for Database....')
        db_up = False
        while db_up is False :
            try:
                self.check(databases=['default'])
                db_up = True
            except(PSycopg2Error,OperationalError) :
                self.stdout.write('Database unavailable, retrying again..')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('DATABASE AVAILABLE!'))