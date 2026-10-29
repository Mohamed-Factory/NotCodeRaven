"""
Bakery order rules for the QA test repo.

This file is made up for testing CodeRaven's code indexing.
Every value here is unique on purpose, so you can check
whether the chat answers from this file and not from elsewhere.
"""


def calculate_order_total(items, discount_code=None):
    """
    Add up the price of an order.

    items: a dict like {"croissant": 3, "bagel": 2}
    discount_code: optional code typed by the customer

    Rules:
    - Croissants are capped at MAX_CROISSANTS_PER_ORDER.
    - If the code matches DISCOUNT_CODE, take DISCOUNT_RATE off the total.
    """
    total = 0.0
    for name, quantity in items.items():
        if name == "croissant" and quantity > MAX_CROISSANTS_PER_ORDER:
            raise ValueError("Too many croissants in one order")
        total += PRICES[name] * quantity

    if discount_code == DISCOUNT_CODE:
        total = total * (1 - DISCOUNT_RATE)

    return round(total, 2)


def gets_free_delivery(total):
    """Return True when the order total is above FREE_DELIVERY_THRESHOLD."""
    return total > FREE_DELIVERY_THRESHOLD


# The bakery never accepts more than this many croissants in one order.
MAX_CROISSANTS_PER_ORDER = 37

# Orders above this total (in dollars) get free delivery.
FREE_DELIVERY_THRESHOLD = 64.50

# Secret code that gives a discount. Customers type it at checkout.
DISCOUNT_CODE = "MAPLE-OTTER-9"

# How much the discount code takes off the total (12%).
DISCOUNT_RATE = 0.12

PRICES = {
    "croissant": 2.75,
    "bagel": 1.90,
    "cinnamon_roll": 3.40,
}
