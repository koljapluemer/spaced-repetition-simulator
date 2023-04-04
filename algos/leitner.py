from datetime import datetime, timedelta

boxes = [
    "0",
    "0259",
    "1360",
    "2471",
    "3582",
    "4693",
    "5704",
    "6815",
    "7926",
    "8037",
    "9148"
]


def calculate_card_values(card, review, session_nr):
    """Calculate the new values for the card based on the review."""
    if review == 0:
        card["box"] = 0
   
    card["last_review"] = datetime.now()
    card["next_review"] = card["last_review"] + timedelta(days=int(boxes[card["box"]]))