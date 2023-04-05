import random
import randomname
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
        card.set_box("current")
    if review == 1:
        # if the cards current box ends with the session_nr, move into retired 
        if boxes.index(card.box) == session_nr:
            card.set_box("retired")

        # if card is in "current", move
        if card.box == "current":
            # move to box that starts with session_nr
            for box in boxes:
                if box.startswith(str(session_nr)):
                    card.set_box(box)
                    break
    return card


def calculate_session_nr(date_time):
    return date_time.day % 10


# FROM RUN

class Card:
    def __init__(self):
        self.name = randomname.get_name()
        # set due to now
        self.interval = 1
        self.box = "current"

    def set_box(self, box):
        self.box = box

    def __repr__(self):
        return f"{self.name}: \n\tInterval: {self.interval} \n"

logs = []

def create_cards(n):
    cards = []
    for i in range(n):
        cards.append(Card())
    return cards

def simulate_reviews_for_day(date_time, cards):
    print('------------------------------')
    print(f"Simulating reviews for {date_time}...")
    print('------------------------------')
  
    session_nr = calculate_session_nr(date_time)
    list_of_boxes_to_review = ["current"]
    # add all boxes that contain the session_nr
    for box in boxes:
        if str(session_nr) in box:
            list_of_boxes_to_review.append(box)

    for card in cards:
        if card.box in list_of_boxes_to_review:
            # simulate a review (randomly pick between 0 and 1)
            review = random.randint(0, 1)
            # update card
            card = calculate_card_values(card, review, session_nr)
            print(card)
            logs.append({
                'card': card,
                'review': review,
                'date_time': date_time,
                'session_nr': session_nr,
                'box': card.box
            })
    

def main():
    cards = create_cards(1)
    # get a list of the next 20 days
    # for each day, simulate reviews
    for i in range(20):
        date_time = datetime.now() + timedelta(days=i)
        simulate_reviews_for_day(date_time, cards)


if __name__ == "__main__":
    main()