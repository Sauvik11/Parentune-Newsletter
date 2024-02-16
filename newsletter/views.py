from django.views import View
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from .models import User, Newsletter, Log
from django.core.mail import send_mail
from django.http import HttpResponse
from .tasks import send_newsletter
from django.views.generic.edit import CreateView
from .forms import NewsletterForm
from django.urls import reverse_lazy
# Create your views here.



class Home(TemplateView):
    template_name = 'newsletter/home.html'


class Subscribe(CreateView):
    model = User
    template_name = 'newsletter/home.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('thankyou')  

    def form_valid(self, form):
       
        form.instance.subscription_status = True 
        return super().form_valid(form)

class ThankYouView(TemplateView):
    template_name = 'newsletter/thankyou.html'

class AddNewsletterView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'newsletter/home.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
class SendNewsletterView(View):

    def get(self, request, *args, **kwargs):
        send_newsletter.delay()
        return HttpResponse("Newsletter sent successfully.")
    
class UnsubscribeView(View):
    def get(self, request, *args, **kwargs):
        # Extract user email from the URL or request data
        email = request.GET.get('email')
        print(email,'mail')
        user = get_object_or_404(User, email=email)
        user.unsubscribe()
        return HttpResponse("You have successfully unsubscribed.")
