import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Creates the window and area that the game will be played on
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
# Disables the echo from user input
curses.noecho()
# Disables the cursor
curses.curs_set(0)
win.nodelay(1)

# Initializing values
snake = [[4, 10], [4, 9], [4, 8]]
food = [10, 20]
score = 0

# Initializing input
win.keypad(1)
key = KEY_RIGHT

# Prints the food on screen
win.addch(food[0], food[1], "*")

# While Esc key is not pressed
while key != 27:
    # Draws the game area
    win.border(0)
    win.addstr(0, 2, " Score: " + str(score) + " ")
    win.addstr(0, 27, " SNAKE ")

    # Increases the speed of Snake as its length increases
    win.timeout(int(150 - (len(snake) / 5 + len(snake) / 10) % 120))

    # Registers user input
    event = win.getch()

    prevKey = key

    # If an invalid key is pressed, do nothing
    if event in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27, ord(" "), ord("p")]:
        key = event

    # If SPACE BAR or P are pressed, pause the game
    if key == ord(" ") or key == ord("p"):
        key = -1
        win.addstr(10, 25, " PAUSED ")

        while key != ord(" ") and key != ord("p") and key != 27:
            key = win.getch()

        # If Esc key is pressed during PAUSE, exit
        if key == 27:
            break

        key = prevKey
        win.addstr(10, 25, "        ")
        continue

    # Adds a new head to snake according to their movement
    if key == KEY_DOWN:
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    elif key == KEY_UP:
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    elif key == KEY_LEFT:
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    elif key == KEY_RIGHT:
        snake.insert(0, [snake[0][0], snake[0][1] + 1])

    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0:
        snake[0][0] = 18
    if snake[0][1] == 0:
        snake[0][1] = 58
    if snake[0][0] == 19:
        snake[0][0] = 1
    if snake[0][1] == 59:
        snake[0][1] = 1

    # If snake runs over itself
    if snake[0] in snake[1:]:
        break

    # If the snake eats the food, its tail is not deleted
    if snake[0] == food:
        score += 1
        food = []

        # The new food coordinates are calculated
        while food == []:
            food = [
                randint(1, 18),
                randint(1, 58),
            ]

            if food in snake:
                food = []

        win.addch(food[0], food[1], "*")
    else:
        # If it does not eat the food, length decreases
        last = snake.pop()
        win.addch(last[0], last[1], " ")

    # Draws snake on the screen
    win.addch(snake[0][0], snake[0][1], "#")

curses.endwin()

# Displays final score if game has not been exited
if key != 27:
    print("Score - " + str(score))