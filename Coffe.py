"""
Coffee menu rules for the QA test repo.

Made-up values for testing whether CodeRaven re-indexes
automatically when a new file is pushed.
"""

# Largest cup size the cafe sells, in ounces.
LARGEST_CUP_OUNCES = 23

# Name of the house blend.
HOUSE_BLEND = "Copper Fox Roast"

# Oat milk costs extra.
OAT_MILK_SURCHARGE = 0.85

# Loyalty card: every Nth coffee is free.
FREE_COFFEE_EVERY = 11

COFFEE_PRICES = {
    "espresso": 2.20,
    "flat_white": 3.95,
    "cold_brew": 4.60,
}


def coffee_price(drink, oat_milk=False):
    """Return the price of a drink, adding the oat milk surcharge if asked."""
    price = COFFEE_PRICES[drink]
    if oat_milk:
        price += OAT_MILK_SURCHARGE
    return round(price, 2)


def is_free_coffee(cups_bought):
    """Return True when this cup is free on the loyalty card."""
    return cups_bought > 0 and cups_bought % FREE_COFFEE_EVERY == 0
