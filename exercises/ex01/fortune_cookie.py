"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730332428"
from random import randint



print("Your fortune cookie says...")
message: int = (randint( 1, 4))
if message > 3:  #4
    print("Your life will be happy and peaceful.")
else:
    if message < 2:  #1
        print("Soon life will become more interesting.")
    else:
        if message == 3:
            print("You will have a gorgeous cat in the near future.")
        else:
            print("A beautiful, smart, and loving person will be coming into your life.")
print("Now, go spread positive vibes!")