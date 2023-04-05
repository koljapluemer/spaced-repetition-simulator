from datetime import timedelta

def calculate_card_values(card, review):
    card.interval = card.interval + 1
    return card