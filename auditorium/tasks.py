from celery import shared_task
from django.core.mail import send_mail

from auditorium.models import Course
from config.settings import EMAIL_HOST_USER


@shared_task
def send_email_for_subscribers(instance):
    course = Course.objects.get(pk=instance)
    for subs in course.subscribe_set.all():
        email = subs.user.email
        send_mail(
            subject='Уведомление об изменении в курсе',
            message=f'Уведомляем, что {course.name} был изменён.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )


@shared_task
def deactivate_inactive_users():
    ...