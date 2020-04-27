import random
from pick import pick

money = 100


num = random.randint(1, 10)
money = 100

#Into selection screen
title = "Select your game: \n" + "You have $" + str(money) + " in your account."
arrow = "$"
options = ["Flip-A-Coin", "Cho-Han",
"Pick A Card (The higher number wins)", "Roulette"]
intro_selection = pick(options, title, arrow)

#def coin_flipping():
