import random
import randomname
import datetime
from datetime import timedelta
import simulators.randomReviews as sim
import algos.addDay as algos
import utils.plot as plot

class Card:
    def __init__(self):
        self.name = randomname.get_name()
        # set due to now
        self.due_at = datetime.datetime.now()
        self.interval = 1

    def __repr__(self):
        return f"{self.name}: \n\tDue: {self.due_at}, \n\tInterval: {self.interval} \n"

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
    # filter cards that are due
    # for each card, simulate a review
    # update the card's due_at and interval
    for card in cards:
        if card.due_at <= date_time:
            # simulate a review
            review = sim.simulate_review()
            # update card
            card = algos.calculate_card_values(card, review)
            print(card)
            logs.append({
                'card': card,
                'review': review,
                'date_time': date_time
            })
    

def main():
    cards = create_cards(1)
    # get a list of the next 20 days
    # for each day, simulate reviews
    for i in range(20):
        date_time = datetime.datetime.now() + timedelta(days=i)
        simulate_reviews_for_day(date_time, cards)

    plot.test_plot(logs)

if __name__ == "__main__":
    main()