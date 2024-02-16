from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from newsletter.tasks import send_newsletter  

class Command(BaseCommand):
    help = 'Run scheduled tasks'

    def handle(self, *args, **options):
        scheduler = BlockingScheduler()
        scheduler.add_job(send_newsletter, 'interval', minutes=1)  # Set the schedule
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass