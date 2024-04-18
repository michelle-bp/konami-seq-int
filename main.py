# # Coding Exercise
#
# In this exercise, you will write a method that
# - while receiving an input sequence
# - listens and sees if a specific sequence occurs, and
# - if so, triggers a callback.
#
# This is inspired by video game cheat codes, for example the Konami Code from
# the 80's. While at the title screen, players could input the button sequence
# 
# ```
# UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A [START]
# ```
# 
# to get infinite lives, all powerups, etc etc.
#
# -----
#
# We have provided the following
# 1. a constant defining the cheat code sequence
# 2. a simulated input sequence of button presses
# 3. a simple callback (it just prints `">>> Callback executed!"`)
#
# Your task is to update the provided code so that we call the callback at the
# right time. We will test your work by running the code (`python -m main`).
#
# We will ask you to do this in stages:
# 1. First, update `main` to print each item in the input sequence.
# 2. Second, update `main` to run the callback after printing every item.
# 3. Finally, update `main` to only run the callback if the last item in the
#    sequence completed the code sequence. Please continue to print each item
#    in the input sequence (for easy debugging).
#
# -----
#
# The expected output is something like the following:
# ```
# A  <-- Start of input sequence
# B
# UP
# LEFT
# DOWN
# UP  <-- Start of cheat code sequence
# UP
# DOWN
# DOWN
# LEFT
# RIGHT
# LEFT
# RIGHT
# B
# A
# [START]  <-- We notice the cheat code is complete, so we run the callback
# >>> Callback executed!
# A
# B
# ...
# ```
# 
# # Evaluation criteria
# 
# Correctness - Do you generate the expected output
#
# Readable - Other engineers should be able to look at your code and understand
# it.
from typing import Iterable


# Constants

KONAMI_SEQUENCE = [
    'UP',
    'UP',
    'DOWN',
    'DOWN',
    'LEFT',
    'RIGHT',
    'LEFT',
    'RIGHT',
    'B',
    'A',
    '[START]',
]


# Utilities

def get_simulated_button_input(fname: str) -> Iterable[str]:
    '''Simulates button input by reading in file & printing it line by line'''
    with open(fname) as f:
        for line in f.read().strip().split('\n'):
            yield line.strip()


def callback() -> None:
    print('>>> Callback executed!')
    

# Main

def main() -> None:
    input_sequence = get_simulated_button_input("./test.csv")
    ### Your code here ###
    pass
    ###


if __name__ == '__main__':
    main()
