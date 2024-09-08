"""
 **Answers to each input:*** (to follow episode 4x11)

 Path 1 - leave:
   - Move the barrel
   - Enter tunnel
   - Read note
   - Leave
   - Look
   - Get on the boat
   - Yes

 Path two - stay:
   - Sit down next to my friend
   - Light a match
   - Stay
"""

from pathlib import Path
from sys import path

codebase_root = Path(__file__).parents[0]
path.append(str(codebase_root))
from utilities.ascii import *


def start():
    print(START_1)
    print(START_3)
    input('Press the "Enter" button to start...')


def barrel():
    print(BARREL_2)
    print(
        "\nYou're trapped in a dungeon with your friend."
        "\nYou see a barrel. What do you do?\n"
    )
    while True:
        if input("> ").strip().lower() == "move the barrel":
            break
        else:
            print("You can't do that here.\n")


def tunnel():
    print(TUNNEL)
    print(
        "\nThe barrel rolls aside and you find a secret tunnel."
        "\nWhat do you do?\n"
    )
    while True:
        if input("> ").strip().lower() == "enter tunnel":
            break
        else:
            print("You can't do that here.\n")


def note():
    print(FRIEND_2)
    print(
        "\nYou start to escape but your friend is too weak to"
        "\ngo with you. They hand you a note."
        "\nWhat do you do?\n"
    )
    while True:
        if input("> ").strip().lower() == "read note":
            break
        else:
            print("You can't do that here.\n")


def too_dark():
    print(NOTE_1)
    print("\nIt is too dark to read the note. " "\nWhat do you do?\n")
    while True:
        if input("> ").strip().lower() == "leave":
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
        if input("> ").strip().lower() == "look":
            break
        else:
            print("You can't do that here.\n")


def look():
    print(BOAT_3)
    print("\nIn the water you see a boat." "\nWhat do you do?\n")
    while True:
        if input("> ").strip().lower() == "get on the boat":
            congratulations()
            break
        else:
            print("You can't do that here.\n")


def congratulations():
    print(CONGRATULATIONS_2)
    print(
        "\nCongratulations, you're heading to a new world!"
        "\nDo you want to play again?\n"
    )
    # TODO: Fix this. Avoid calling main() within subfunction.
    if input("> ").strip().lower() == "yes":
        main()
    else:
        quit()


def barrel_2():
    print(BARREL_2)
    # print(YOUR_FRIEND_2)
    print(YOUR_FRIEND_3)
    print(YOUR_FRIEND_5)
    print(
        "\nYou're trapped in a dungeon with your friend."
        "\nYou see a barrel. What do you do?\n"
    )
    while True:
        if input("> ").strip().lower() == "sit down next to my friend":
            break
        else:
            print("You can't do that here.\n")


def note_2():
    print(NOTE_1)
    print("\nYour friend hands you a note." "\nWhat do you do?\n")
    while True:
        if input("> ").strip().lower() == "light a match":
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
        if input("> ").strip().lower() == "stay":
            break
        else:
            print("You can't do that here.\n")


def stay():
    # print(STAY_1)
    print(ELLIOT_2)
    print("It's an exciting time in the world.")
    print(END_1)
    quit()


def path_leave():
    start()
    barrel()
    tunnel()
    note()
    too_dark()
    leave()
    look()


def path_stay():
    start()
    barrel_2()
    note_2()
    match()
    stay()


def main():
    path_leave()
    # path_stay()


if __name__ == '__main__':
    main()
