import json
from datetime import datetime, timedelta

import stripe
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_link(product_object):
    product = stripe.Product.create(
        name=product_object.name,
        description=product_object.description
    )
    price = stripe.Price.create(
        unit_amount=product_object.price * 100,
        currency="rub",
        product=product['id'],
    )
    link = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{'quantity': 1, "price": price, }],
        mode="payment",
    )

    return link['url']


# Создаем интервал для повтора
schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)

# Создаем задачу для повторения
PeriodicTask.objects.create(
    interval=schedule,
    name='Усыпляем старых пользователей',
    task='auditrioum.tasks.deactivate_inactive_users',
    args=json.dumps(['arg1', 'arg2']),
    kwargs=json.dumps({
        'be_careful': True,
    }),
    expires=datetime.utcnow() + timedelta(seconds=30)
)
