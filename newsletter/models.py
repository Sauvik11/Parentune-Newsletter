from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    subscription_status = models.BooleanField(default=False)

    def unsubscribe(self):
        self.subscription_status = False
        self.save()

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    email_status = models.CharField(max_length=20, default='Pending')

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

class JobScheduler(models.Model):
    scheduled_time = models.DateTimeField()

