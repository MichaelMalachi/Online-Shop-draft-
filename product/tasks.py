

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        'Добро пожаловать на наш сайт!',
        'Спасибо за регистрацию.',
        'no-reply@mysite.com',
        [email],
        fail_silently=False,
    )
