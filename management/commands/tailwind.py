from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone
import subprocess
import sys
import os

class Command(BaseCommand):

    help = 'Displays current time'

    def add_arguments(self, parser):
        # Positional arguments
        #parser.add_argument('run', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument(
            '--dev',
            action='store_true',
            help='run npm dev',
        )

    def handle(self, *args, **options):
        if options['dev']:
            #path = sys.path.append(os.path.join(os.path.dirname('frontend'), "frontend"))
            path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            #path = os.path.join(settings.BASE_DIR, 'frontend')
            subprocess.Popen('npm run dev', shell=True, cwd=path)
