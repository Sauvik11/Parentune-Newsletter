from django.urls import path
from .views import Home,SendNewsletterView,Subscribe,ThankYouView, AddNewsletterView,UnsubscribeView
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('subscribe/',Subscribe.as_view(), name='subscribe'),  # Add this line
    path('send_newsletter/', SendNewsletterView.as_view(), name='send_newsletter'),
    path('thankyou/', ThankYouView.as_view(), name='thankyou'),
    path('unsubscribe/', UnsubscribeView.as_view(), name='unsubscribe'),
    path('add-newsletter/', AddNewsletterView.as_view(), name='add_newsletter'),
    # Add other URLs as needed 
]