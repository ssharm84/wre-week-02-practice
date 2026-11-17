def delivery_fee(subtotal_cents):
    """Charge $5 for delivery, with free delivery from $60."""
    if subtotal_cents < 0:
        raise ValueError("Order subtotal cannot be negative")
    if subtotal_cents >= 6000:
        return 0
    return 500
