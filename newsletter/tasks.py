from celery import shared_task
from django.core.mail import send_mail
from .models import User, Newsletter, Log
import schedule
import time 
import logging
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.models import Site 

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_newsletter(self):
    latest_newsletter = Newsletter.objects.latest('sent_at')
    # Get all subscribed users
    subscribed_users = User.objects.filter(subscription_status=True)

 
    for user in subscribed_users:
        log = Log.objects.create(user=user, email_status='Pending')
        current_site = Site.objects.get_current()
        unsubscribe_url = f"http://{current_site.domain}/unsubscribe/?email={user.email}"
        subject = latest_newsletter.title
        from_email = 'parentune@gmail.com'
        to_email = [user.email]
        context = {'user': user, 'newsletter': latest_newsletter, 'unsubscribe_url': unsubscribe_url}
        message = render_to_string('newsletter/email_template.html', context)
        email = EmailMessage(subject, message, from_email, to_email)
        email.content_subtype = 'html'
        email.send()
        log.user = user
        log.email_status = 'Sent'
        log.save()



