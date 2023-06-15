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


# main routine
rounds_played = 0
rounds_won = 0
rounds_lost = 0

# lists for checking responses
tf_list = ["true", "false", "xxx"]
dif_list = ["easy", "medium", "hard"]

# Ask users for difficulty of questions
print()
print("Choose your difficulty:")
difficulty = choice_checker("====== easy | medium | hard ======", dif_list,
                            "Please enter a valid difficulty")
print(f"\t======= {difficulty} mode =======")

end_game = "no"
if difficulty == "easy":
    while end_game == "no":

        # random integers for equation generators
        integer_1 = (random.randint(50, 100))
        integer_2 = (random.randint(50, 100))
        integer_3 = (random.randint(50, 100))
        integer_4 = (random.randint(50, 100))
        integer_5 = (random.randint(50, 100))
        integer_6 = (random.randint(50, 100))
        integer_7 = (random.randint(50, 100))
        integer_8 = (random.randint(50, 100))
        integer_9 = (random.randint(75, 100))
        integer_10 = (random.randint(75, 100))
        integer_11 = (random.randint(50, 74))
        integer_12 = (random.randint(50, 74))

        # randomizes questions so that it spread equally ( +, -, <, >)
        randomizer = random.randint(1, 80)

        # ensures that equations are randomized via true or false equations
        equation = random.choice(tf_list[:-1])
        response = tf_list

        # displays true equations randomly
        if equation == "true":

            if 1 < randomizer < 20:
                choice_checker(
                    f" {integer_1} + {integer_2} ={integer_1 + integer_2} (spoiler {equation}){rounds_played}"
                    f"| True or False?", tf_list, "please enter true or false")
            elif 21 < randomizer < 60:
                choice_checker(
                    f" {integer_3} - {integer_4} ={integer_3 - integer_4} (spoiler {equation}){rounds_played}"
                    f"| True or False?", tf_list, "please enter true or false")
            else:
                choice_checker(f" {integer_9} + {integer_10} > "
                               f"{integer_11} + {integer_12} (spoiler {equation}){rounds_played}"
                               f"| True or False?", tf_list, "please enter true or false")

        # displays false equations randomly
        if equation == "false":
            if 1 < randomizer < 40:
                choice_checker(
                    f" {integer_5} + {integer_6} ={integer_4 + integer_6} (spoiler {equation}) {rounds_played}"
                    f"| True or False?", tf_list, "please enter true or false")
        else:
            choice_checker(f" {integer_7} - {integer_8} ={integer_3 - integer_8} (spoiler {equation}) {rounds_played}"
                           f"| True or False?", tf_list, "please enter true or false")

        rounds_played += 1
