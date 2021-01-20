# Python Snake Multiplayer

The objective for this project is to modify an [already existing Snake game code in Python](https://gist.github.com/sanchitgangwar/2158088) so it supports multiplayer, using mechanics from both the Snake game and the Tron Cycle game.

## Getting Started (for Windows)

[Download the *curses* package](https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses) relative to the version of Python you're using and install it with the following command (in the directory to where you downloaded it to):

```
python -m pip install curses-[curses_version]-cp[python_version]-win32/64.whl
```

## How to Run

To run the program, run the following command:

```
python snake.py
```

The program accepts the following parameters (the order must be the same):
* Use colors ("true" or "false", default = false)
* Frame interval (milliseconds per frame, default = 75)

The following example runs the program with colors enabled with speed of 100 milliseconds per frame:

```
python snake.py true 100
```

## Sources

Based on: https://gist.github.com/sanchitgangwar/2158088