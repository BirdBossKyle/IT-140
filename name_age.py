# Ask the user for their name and age, then calculate their birth year.

from datetime import datetime

name = input("What is your name? ")
age = int(input("How old are you? "))

current_year = datetime.now().year
birth_year = current_year - age

print(f"Hello {name}! You were born in {birth_year}.")
