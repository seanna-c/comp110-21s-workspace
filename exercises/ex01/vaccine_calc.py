"""A vaccination calculator."""

__author__ = "730332428"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))
dose_ad: int = int(input("Doses administered: "))
dose_pday: int = int(input("Doses per day: "))
targ_percent: int = int(input("Target percent vaccinated: "))
num_of_days: float = ((population * (targ_percent * 0.01)) - (dose_ad/2)) * (2 / dose_pday)
int_of_days: int = round(num_of_days)
today: datetime = datetime.today()
future_days : timedelta = timedelta(int_of_days)

future: datetime = today + future_days
future1: str = future.strftime("%B %d, %Y")

print("We will reach " + str(targ_percent)+ "% vaccination in " + str(int_of_days) + " days, which falls on " + str(future1) + ".")

