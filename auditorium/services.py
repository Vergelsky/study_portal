import stripe

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
