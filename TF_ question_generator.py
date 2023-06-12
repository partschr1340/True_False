# Checks that users inputs are valid, display error if user input is invalid
import random


def choice_checker(question, valid_list, error):
    while True:
        # Ask user fpr choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item),
        # the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)


# lists for checking responses
tf_list = ["true", "false", "tru", "xxx"]
dif_list = ["easy", "medium", "hard"]
# Ask users for difficulty of questions
print()
print("Choose your difficulty:")
difficulty = choice_checker("====== easy | medium | hard ======", dif_list,
                            "Please enter a valid difficulty")
print(f"\t======= {difficulty} mode =======")

if difficulty == "easy":
    while True:
        randomizer = random.randint(1, 80)

        integer_1 = (random.randint(50, 100))
        integer_2 = (random.randint(50, 100))

        integer_3 = (random.randint(50, 100))
        integer_4 = (random.randint(50, 100))

        integer_5 = (random.randint(50, 100))
        integer_6 = (random.randint(50, 100))

        integer_7 = (random.randint(50, 100))
        integer_8 = (random.randint(50, 100))

        wrong = random.randint(75, 197)

        equation = random.choice(tf_list)
        if 1 < randomizer < 20:
            choice_checker(f"{integer_1} + {integer_2} = {integer_1 + integer_2} | t or f?  ", tf_list,
                           "please enter valid answer")
        elif 21 < randomizer < 60:
            choice_checker(f"{integer_1} + {integer_2} = {wrong} | t or f? ", tf_list,
                                   "please enter valid answer")
        else:
            if 61 < randomizer < 80:
                choice_checker(f"{integer_3} - {integer_4} = {integer_3 - integer_4} | t or f? ", tf_list,
                               "please enter a valid answer")
