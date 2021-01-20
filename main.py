# This is a bill roulette, it will choose randomly a person to pay the bill.



names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

x = len(names)

picked = random.randint(0, x) 

print(f"The person to pay the bill today is {names[picked]}")

