"""
Bakery order rules for the QA test repo.

Control test: every value is returned from its own small function.
"""


def get_prices():
    """Price of each bakery item in dollars."""
    return {"croissant": 2.75, "bagel": 1.90, "cinnamon_roll": 3.40}


def get_discount_code():
    """The discount code customers type at checkout."""
    return "MAPLE-OTTER-9"


def get_discount_rate():
    """How much the discount code takes off the total: 12 percent."""
    return 0.12


def get_max_croissants():
    """Most croissants allowed in one order."""
    return 37


def get_free_delivery_threshold():
    """Orders above this total in dollars get free delivery."""
    return 64.50
