"""
 **Answers to each input:*** (to follow episode 4x11)

 Iteration 1:
   - Move the barrel
   - Enter tunnel
   - Read note
   - Leave
   - Look
   - Get on the boat
   - Yes

 Iteration 2:
   - Sit down next to my friend
   - Light a match
   - Stay
"""

import os
import sys

import ascii_images


def congratulations():
    print(
        "\nCongratulations, you're heading to a new world!"
        "\nDo you want to play again?\n"
    )
    if input("> ").lower() == "yes":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    else:
        quit()


def start():
    print(ascii_images.start)
    print(ascii_images.exit)
    input('Press the "Enter" button to start...')


# def trapped():
#     print(
#         "\nYou're trapped in a dungeon with your friend."
#         "\nYou see a barrel. What do you do?"
#     )


def barrel():
    print(
        "\nYou're trapped in a dungeon with your friend."
        "\nYou see a barrel. What do you do?\n"
    )
    while True:
        if input("> ").lower() == "move the barrel":
            break
        else:
            print("You can't do that here.\n")


def tunnel():
    print(
        "\nThe barrel rolls aside and you find a secret tunnel."
        "\nWhat do you do?\n"
    )
    while True:
        if input("> ").lower() == "enter tunnel":
            break
        else:
            print("You can't do that here.\n")


def note():
    print(
        "\nYou start to escape but your friend is too weak to"
        "\ngo with you. They hand you a note."
        "\nWhat do you do?\n"
    )
    while True:
        if input("> ").lower() == "read note":
            break
        else:
            print("You can't do that here.\n")


def too_dark():
    print("\nIt is too dark to read the note. " "\nWhat do you do?\n")
    while True:
        if input("> ").lower() == "leave":
            break
        else:
            print("You can't do that here.\n")


def leave():
    print(
        "\nYou crawl through the tunnel and the tunnel leads"
        "\nyou to a beach. What do you do?\n"
    )
    while True:
        if input("> ").lower() == "look":
            break
        else:
            print("You can't do that here.\n")


def look():
    print("\nIn the water you see a boat." "\nWhat do you do?\n")
    while True:
        if input("> ").lower() == "get on the boat":
            # break
            congratulations()
        else:
            print("You can't do that here.\n")


def barrel_2():
    print(
        "\nYou're trapped in a dungeon with your friend."
        "\nYou see a barrel. What do you do?\n"
    )
    while True:
        if input("> ").lower() == "sit down next to my friend":
            break
        else:
            print("You can't do that here.\n")


def note_2():
    print("\nYour friend hands you a note." "\nWhat do you do?\n")
    while True:
        if input("> ").lower() == "light a match":
            break
        else:
            print("You can't do that here.\n")


def match():
    print(
        "\nThe note says, 'Don't leave me here.'"
        "\nDo you leave your friend or stay?\n"
    )
    while True:
        if input("> ").lower() == "stay":
            break
        else:
            print("You can't do that here.\n")


def stay():
    print("It's an exciting time in the world.")
    print(ascii_images.end)
    quit()


def main_1():
    start()
    barrel()
    tunnel()
    note()
    too_dark()
    leave()
    look()
    # If iteration_1:
    # Else iteration_2
    # bye()


def main_2():
    start()
    barrel_2()
    note_2()
    match()
    stay()


if __name__ == '__main__':
    # main_1()
    main_2()
    # start()
    # trapped()
    # dungeon()
    # bye()
    # note()
    # leave()
    # look()
    # get()
