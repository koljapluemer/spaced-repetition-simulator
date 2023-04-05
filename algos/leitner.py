from datetime import datetime, timedelta

boxes = [
    "current",
    "0259",
    "1360",
    "2471",
    "3582",
    "4693",
    "5704",
    "6815",
    "7926",
    "8037",
    "9148",
    "retired"
]


def calculate_card_values(card, review, session_nr):
    """Calculate the new values for the card based on the review."""
    if review == 0:
        card["box"] = 0
    if review == 1:
        # if the cards current box ends with the session_nr, move into retired 
        if boxes[card["box"]].endswith(str(session_nr)):
            card["box"] = len(boxes) - 1

        # if card is in "current", move
        if card["box"] == "current":
            # move to box that starts with session_nr
            for i in range(1, len(boxes)):
                if boxes[i].startswith(str(session_nr)):
                    card["box"] = i
                    break
   
    card["last_review"] = datetime.now()
    card["next_review"] = card["last_review"] + timedelta(days=int(boxes[card["box"]]))


def calculate_session_nr(datetime):
    # get datetime from string
    date = datetime.strptime(datetime, "%Y-%m-%d %H:%M:%S.%f")
    # calculate number from 0-9 based on current date
    return date.day % 10

def check_if_card_is_due(card):
    session_nr = calculate_session_nr(card["last_review"])