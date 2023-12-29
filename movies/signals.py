# signals.py
from django.db.models.signals import Signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from api_crud.views import send_model_instance_created_email
from .models import Movie
model_instance_created = Signal()

@receiver(post_save, sender=Movie)
def send_email_on_model_instance_create(sender, instance, created, **kwargs):
    print('##################recived signal')
    
    model_instance_created.connect(send_model_instance_created_email)
    if created:
        model_instance_created.send(sender=instance.__class__, instance=instance)