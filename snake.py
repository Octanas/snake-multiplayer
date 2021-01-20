import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Declare constants
KEY_W = ord("w")
KEY_S = ord("s")
KEY_A = ord("a")
KEY_D = ord("d")
KEY_P = ord("p")
SPACE_BAR = ord(" ")
ESC = 27

# Creates the window and area that the game will be played on
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
# Disables the echo from user input
curses.noecho()
# Disables the cursor
curses.curs_set(0)
win.nodelay(1)

# Initializing values
snake_p1 = [[4, 10], [4, 9], [4, 8]]
snake_p2 = [[16, 10], [16, 9], [16, 8]]
food = [10, 20]
food_eaten_p1 = 0
food_eaten_p2 = 0

# Winner:
# 0 - DRAW
# 1 - P1
# 2 - P2
winner = 0

# Initializing input
# P1 and P2 key are used for each snake
win.keypad(1)
key_p1 = KEY_RIGHT
key_p2 = KEY_D

# Prints the food on screen
win.addch(food[0], food[1], "*")

# Run forever
while True:
    # Draws the game area
    win.border(0)
    win.addstr(0, 2, " Food Eaten P1: " + str(food_eaten_p1) + " ")
    win.addstr(
        0,
        40 - (len(str(food_eaten_p2)) - 1),
        " Food Eaten P2: " + str(food_eaten_p2) + " ",
    )
    win.addstr(0, 26, " SNAKE ")

    # Increases the speed of Snake as its length increases
    win.timeout(
        int(
            150
            - (len(max(snake_p1, snake_p2)) / 5 + len(max(snake_p1, snake_p2)) / 10)
            % 120
        )
    )

    # Registers user input
    key_event = win.getch()

    # If an invalid key is pressed, do nothing
    if key_event in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN]:
        backwards = (
            key_p1 == KEY_LEFT
            and key_event == KEY_RIGHT
            or key_p1 == KEY_RIGHT
            and key_event == KEY_LEFT
            or key_p1 == KEY_UP
            and key_event == KEY_DOWN
            or key_p1 == KEY_DOWN
            and key_event == KEY_UP
        )

        if not backwards:
            key_p1 = key_event
    elif key_event in [KEY_W, KEY_S, KEY_A, KEY_D]:
        backwards = (
            key_p2 == KEY_A
            and key_event == KEY_D
            or key_p2 == KEY_D
            and key_event == KEY_A
            or key_p2 == KEY_W
            and key_event == KEY_S
            or key_p2 == KEY_S
            and key_event == KEY_W
        )

        if not backwards:
            key_p2 = key_event
    # If SPACE BAR or P are pressed, pause the game
    elif key_event == SPACE_BAR or key_event == KEY_P:
        key_event = -1
        win.addstr(10, 25, " PAUSED ")

        while key_event != SPACE_BAR and key_event != KEY_P and key_event != ESC:
            key_event = win.getch()

        win.addstr(10, 25, "        ")

    # If ESC key is pressed, exit
    if key_event == ESC:
        winner = -1
        break

    # Adds a new head to snake P1 according to their movement
    if key_p1 == KEY_DOWN:
        snake_p1.insert(0, [snake_p1[0][0] + 1, snake_p1[0][1]])
    elif key_p1 == KEY_UP:
        snake_p1.insert(0, [snake_p1[0][0] - 1, snake_p1[0][1]])
    elif key_p1 == KEY_LEFT:
        snake_p1.insert(0, [snake_p1[0][0], snake_p1[0][1] - 1])
    elif key_p1 == KEY_RIGHT:
        snake_p1.insert(0, [snake_p1[0][0], snake_p1[0][1] + 1])

    # Adds a new head to snake P1 according to their movement
    if key_p2 == KEY_S:
        snake_p2.insert(0, [snake_p2[0][0] + 1, snake_p2[0][1]])
    elif key_p2 == KEY_W:
        snake_p2.insert(0, [snake_p2[0][0] - 1, snake_p2[0][1]])
    elif key_p2 == KEY_A:
        snake_p2.insert(0, [snake_p2[0][0], snake_p2[0][1] - 1])
    elif key_p2 == KEY_D:
        snake_p2.insert(0, [snake_p2[0][0], snake_p2[0][1] + 1])

    # If a snake crosses the boundaries, make it enter from the other side
    if snake_p1[0][0] == 0:
        snake_p1[0][0] = 18
    elif snake_p1[0][0] == 19:
        snake_p1[0][0] = 1
    if snake_p1[0][1] == 0:
        snake_p1[0][1] = 58
    elif snake_p1[0][1] == 59:
        snake_p1[0][1] = 1

    if snake_p2[0][0] == 0:
        snake_p2[0][0] = 18
    elif snake_p2[0][0] == 19:
        snake_p2[0][0] = 1
    if snake_p2[0][1] == 0:
        snake_p2[0][1] = 58
    elif snake_p2[0][1] == 59:
        snake_p2[0][1] = 1

    eaten = False

    # If a player eats the food, their tail is not deleted
    if snake_p1[0] == food:
        food_eaten_p1 += 1
        eaten = True
    else:
        last = snake_p1.pop()
        win.addch(last[0], last[1], " ")

    if snake_p2[0] == food:
        food_eaten_p2 += 1
        eaten = True
    else:
        last = snake_p2.pop()
        win.addch(last[0], last[1], " ")

    if eaten:
        food = []

        # The new food coordinates are calculated
        while food == []:
            food = [
                randint(1, 18),
                randint(1, 58),
            ]

            if food in snake_p1 or food in snake_p2:
                food = []

        win.addch(food[0], food[1], "*")

    # Draws snakes on the screen
    win.addch(snake_p1[1][0], snake_p1[1][1], "#")
    win.addch(snake_p1[0][0], snake_p1[0][1], "0")

    win.addch(snake_p2[1][0], snake_p2[1][1], "#")
    win.addch(snake_p2[0][0], snake_p2[0][1], "0")

    # If the players' heads touch, its a draw
    if snake_p1[0] == snake_p2[0]:
        win.addch(snake_p1[0][0], snake_p1[0][1], "X")
        winner = 0
        break

    # If a player touches itself or the other snake, the game ends
    if snake_p1[0] in snake_p1[1:] or snake_p1[0] in snake_p2[1:]:
        win.addch(snake_p1[0][0], snake_p1[0][1], "X")
        winner = 2
        break

    if snake_p2[0] in snake_p2[1:] or snake_p2[0] in snake_p1[1:]:
        win.addch(snake_p2[0][0], snake_p2[0][1], "X")
        winner = 1
        break

# Displays final result if game has not been exited
if winner != -1:
    if winner == 0:
        win.addstr(10, 26, "DRAW")
    elif winner == 1:
        win.addstr(10, 24, "P1 WINS")
    elif winner == 2:
        win.addstr(10, 24, "P2 WINS")

    win.addstr(12, 20, "P1 Food Eaten: " + str(food_eaten_p1))
    win.addstr(13, 20, "P2 Food Eaten: " + str(food_eaten_p2))
    win.addstr(15, 19, "Press SPACE to exit")

key_event = -1

while key_event != SPACE_BAR:
    key_event = win.getch()

curses.endwin()