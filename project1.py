import random

subject = [
    "Prime Minister",
    "School Teacher",
    "Doctor",
    "Police Officer",
    "Army Chief",
    "Cricketer",
    "Actor",
    "University Student",
    "Mayor",
    "Tech CEO",
]

action = [
    "banned",
    "arrested",
    "discovered",
    "resigned",
    "launched",
    "declared",
    "escaped",
    "collapsed",
    "apologized",
    "donated",
]

places = [
   "Islamabad",
   "Lahore",
   "Karachi",
   "Peshawar",
   "New York",
   "Dubai",
   "London",
   "Quetta",
   "Delhi",
   "Tokyo ",
]

while True:
    subjects= random.choice(subject)
    actions = random.choice(action)
    place = random.choice(places)

    headLine = "BREAKING NEWS: {} {} in {}!".format(subjects, actions, place)

    print("\n "+ headLine)

    Input_user = input("\nDo you want another? (yes or no): ").strip().lower()

    # .strip remove extra space if user put extra soace
    if Input_user == "no":
        break

    print("\n thanks for using the fake headline generator Goddbyee")
    break