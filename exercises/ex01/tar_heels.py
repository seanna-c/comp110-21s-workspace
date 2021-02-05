"""An exercise in remainders and boolean logic."""

__author__ = "730332428"


value: int = int(input("Enter an int: "))
if value % 2 == 0 and value % 7 == 0:
    print("TAR HEELS")
else:
    if value % 2 == 0:
        print("TAR")
    else:
        if value % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")

