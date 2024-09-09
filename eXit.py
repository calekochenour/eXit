"""
 Answers to each input (to follow episode 4x11) sequence:

 Path 1 - leave for a new world:
   > Move the barrel
   > Enter tunnel
   > Read note
   > Leave
   > Look
   > Get on the boat
   > Yes

 Path two - stay with your friend:
   > Sit down next to my friend
   > Light a match
   > Stay
"""

from pathlib import Path
from sys import path

codebase_root = Path(__file__).parents[0]
path.append(str(codebase_root))
from utilities.ascii import *


def get_response():
    return input("> ").strip().lower()


def start():
    print(START_3)
    print(START_1)
    input("Press the Enter button to start...")


def barrel():
    print(BARREL_2)
    print(
        "\nYou're trapped in a dungeon with your friend."
        "\nYou see a barrel. What do you do?\n"
    )
    while True:
        response = get_response()
        if response == "move the barrel":
            return 0
        elif response == "sit down next to my friend":
            return 1
        else:
            print("You can't do that here.\n")


def tunnel():
    print(TUNNEL)
    print(
        "\nThe barrel rolls aside and you find a secret tunnel."
        "\nWhat do you do?\n"
    )
    while True:
        if get_response() == "enter tunnel":
            break
        else:
            print("You can't do that here.\n")


def note_leave():
    print(FRIEND_2)
    print(
        "\nYou start to escape but your friend is too weak to"
        "\ngo with you. They hand you a note."
        "\nWhat do you do?\n"
    )
    while True:
        if get_response() == "read note":
            break
        else:
            print("You can't do that here.\n")


def too_dark():
    print(NOTE_1)
    print("\nIt is too dark to read the note. " "\nWhat do you do?\n")
    while True:
        if get_response() == "leave":
            break
        else:
            print("You can't do that here.\n")


def leave():
    print(BEACH_1)
    print(
        "\nYou crawl through the tunnel and the tunnel leads"
        "\nyou to a beach. What do you do?\n"
    )
    while True:
        if get_response() == "look":
            break
        else:
            print("You can't do that here.\n")


def look():
    print(BOAT_3)
    print("\nIn the water you see a boat." "\nWhat do you do?\n")
    while True:
        if get_response() == "get on the boat":
            break
        else:
            print("You can't do that here.\n")


def congratulations():
    print(CONGRATULATIONS_2)
    print(
        "\nCongratulations, you're heading to a new world!"
        "\nDo you want to play again?\n"
    )
    if get_response() == "yes":
        eXit()
    else:
        quit()


def note_stay():
    print(NOTE_1)
    print("\nYour friend hands you a note." "\nWhat do you do?\n")
    while True:
        if get_response() == "light a match":
            break
        else:
            print("You can't do that here.\n")


def match():
    print(NOTE_MATCH_2)
    print(
        "\nThe note says, 'Don't leave me here.'"
        "\nDo you leave your friend or stay?\n"
    )
    while True:
        if get_response() == "stay":
            break
        else:
            print("You can't do that here.\n")


def stay():
    print(ELLIOT_2)
    print("It's an exciting time in the world.")
    print(END_1)
    quit()


def leave_for_new_world():
    tunnel()
    note_leave()
    too_dark()
    leave()
    look()
    congratulations()


def stay_with_your_friend():
    note_stay()
    match()
    stay()


def eXit():
    is_real_exit = barrel()
    if is_real_exit:
        stay_with_your_friend()
    else:
        leave_for_new_world()


if __name__ == '__main__':
    start()
    eXit()
