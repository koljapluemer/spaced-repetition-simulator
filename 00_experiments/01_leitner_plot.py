import random
import randomname
from datetime import datetime, timedelta

from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.collections import PolyCollection
import math

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


def get_random_dark_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return [r/1.2, g/1.2, b/1.2]

# fill with 12 empty objects and give random color
datasets = [{'x': [], 'y':[], 'z':[], 'color': get_random_dark_color()} for i in range(12)]

def calculate_card_values(card, review, session_nr):
    """Calculate the new values for the card based on the review."""
    if review == 0:
        card.set_box("current")
    if review == 1:
        # if card is in "current", move
        if card.box == "current":
            # move to box that starts with session_nr
            for box in boxes:
                if box.startswith(str(session_nr)):
                    card.set_box(box)
                    break
        # if the cards current box ends with the session_nr, move into retired 
        elif card.box.endswith(str(session_nr)):
            card.set_box("retired")

    
    return card


def calculate_session_nr(date_time):
    return date_time.day % 10


# FROM RUN

class Card:
    def __init__(self):
        self.name = randomname.get_name()
        self.box = "current"

    def set_box(self, box):
        self.box = box

    def __repr__(self):
        return f"{self.name}: \n in Box: {self.box} \n"

logs = []

def create_cards(n):
    cards = []
    for i in range(n):
        cards.append(Card())
    return cards

def simulate_reviews_for_day(date_time, cards, day_count):
    print('------------------------------')
    print(f"Simulating reviews for {date_time}...")
    print('------------------------------')
  
    session_nr = calculate_session_nr(date_time)
    print(f"Session nr: {session_nr}")

    list_of_boxes_to_review = ["current"]
    # add all boxes that contain the session_nr
    for box in boxes:
        if str(session_nr) in box:
            list_of_boxes_to_review.append(box)
    # count how many cards are in the boxes to review with list comprehension
    counter = len([card for card in cards if card.box in list_of_boxes_to_review])
    print(f"Cards to review: {counter}\n -------- ")

    # for every box, track how many cards are in that box
    for box in boxes:
        counter = len([card for card in cards if card.box == box])
        index_of_box = boxes.index(box)
        datasets[index_of_box]['x'].append(day_count)
        datasets[index_of_box]['z'].append(counter)
        datasets[index_of_box]['y'].append(index_of_box)
        print(f"{box}: {counter}")

    print('------------------')

    for card in cards:
        if card.box in list_of_boxes_to_review:
            # simulate a review (randomly pick between 0 and 1)
            review = random.randint(0, 1)
            # update card
            card = calculate_card_values(card, review, session_nr)
            logs.append({
                'card': card,
                'review': review,
                'date_time': date_time,
                'session_nr': session_nr,
                'box': card.box
            })


def my_plot():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    z = [1, 8, 27, 64, 125]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()


def random_line_chart():

    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

    data = [{"x":[1+i,2,3], "y":[1+i,4,9], "z":[0,i,i*2], "color": "red"} for i in range(6)]

    for dataset in data:
        ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["color"])

    plt.show()

def plot_leitner_due_cards_per_box():
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

    print(f"there are {len(datasets)} datasets ")

    for dataset in datasets:
        ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["color"])
        ax.set(
            xlabel='Day',
            ylabel='Box',
            zlabel='Cards'
        )
    plt.show()


def main():
    cards = create_cards(1000)
    # get a list of the next 20 days
    # for each day, simulate reviews
    day_count = 0
    for i in range(365):
        day_count += 1
        date_time = datetime.now() + timedelta(days=i)
        simulate_reviews_for_day(date_time, cards, day_count)

    plot_leitner_due_cards_per_box()


if __name__ == "__main__":
    main()