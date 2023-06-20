# Online Python compiler (interpreter) to run Python online.# Functions
import random

print("=====WELCOME TO THE TRUE OR FALSE QUIZ =====")


# Instructions
def instructions():
    print("~~~~~~INSTRUCTIONS~~~~~~~")
    print("- You will choose your own difficulty (easy | medium | hard")
    print("- The difficulty you choose will influence the type of questions there are.")
    print(
        "- You will then choose the amount of rounds you want to play at this difficulty or press <enter> for infinite "
        "mode.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("- Easy will include simple addition and subtraction.")
    print("- Medium will include some harder addition and subtraction, as well as some ")
    print("  multiplication and division.")
    print("- Hard will include all the above with much harder difficulty.")
    print("- All difficulties will include greater than or less than questions (<, >, =)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("- Equations will then be generated and you will have to find out if they are")
    print("  true or false")
    print("~~~~~~~Have fun!!!~~~~~~~~~")


# Checks that users inputs are valid, display error if user input is invalid
def choice_checker(question, valid_list, error):
    while True:
        # Ask user fpr choice (and put choice in lowercase)
        user_input = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item),
        # the full item name is returned
        for item in valid_list:
            if user_input == item[0] or user_input == item:
                return item
                # output error if item not in list
        print(error)


def rounds_checker():
    while True:
        rounds_amount = input("How many rounds would you like to play?")
        round_error = "Please enter an integer more than 0 or <enter> for infinite mode"

        # If infinite mode not chose, check response is an integer that is more than 0
        if rounds_amount != "":
            try:
                rounds_amount = int(rounds_amount)
                if rounds_amount < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return rounds_amount


# lists for checking responses
yes_no_list = ["yes", "no"]
tf_list = ["true", "false", "xxx"]
dif_list = ["medium", "hard", "easy"]

# Ask user if they have played game before, if yes continue, if no display instructions
played_before = choice_checker("~~Do you know how the quiz works?", yes_no_list, "~~Please enter yes or no~~")

if played_before == "no":
    instructions()

# What difficultly the user wants the question to be, ensures they enter valid difficulty
print()
print("Choose your difficulty:")
difficulty = choice_checker("====== easy | medium | hard ======", dif_list, "Please enter a valid difficulty")
print(f"\t======= {difficulty} mode =======")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Ask user how many rounds they wish to play at this difficulty
# round integers
rounds = rounds_checker()
mode = "regular"

if rounds == "":
    mode = "infinite"
    rounds = "unlimited"

rounds_played = 0
rounds_won = 0
rounds_lost = 0

# states how many rounds the user has chosen
print(f"{rounds} rounds | {mode} mode")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_1} + {integer_2} ={integer_1 + integer_2}"
                    f" (spoiler {equation}) | True or False?", tf_list, "please enter true or false")

                rounds_played += 1

            elif 21 < randomizer < 60:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_3} - {integer_4} ={integer_3 - integer_4} "
                    f"(spoiler {equation}) | True or False?", tf_list, "please enter true or false")
                rounds_played += 1

            else:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_9} + {integer_10} > {integer_11} + {integer_12} "
                    f"(spoiler {equation}) | True or false?", tf_list, "please enter true or false")
                rounds_played += 1

        # displays false equations randomly
        elif equation == "false":
            if 1 < randomizer < 40:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_5} + {integer_6} ={integer_4 + integer_6} (spoiler {equation})"
                    f"| True or False?", tf_list, "please enter true or false")
                rounds_played += 1

            else:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} | "
                    f"{integer_7} - {integer_8} ={integer_3 - integer_8} (spoiler {equation})"
                    f"| True or False?", tf_list, "please enter true or false")
                rounds_played += 1

        # displays a message if user got it right
        if user_choice == equation:
            print(f" you got it, nice! 👍👍| correct {rounds_won + 1}| incorrect {rounds_lost}")
            print("==========================================")
            rounds_won += 1

        # end game code, only display chicken if user decided to end game on regular mode
        elif user_choice == "xxx":
            if mode == "infinite":
                print("~ Bye bye!")
                end_game = "yes"
                break

            else:
                print("🐔🐔🐔You chickened out!!🐔🐔🐔")
                end_game = "yes"
                break

        # displays an incorrect message if user gets it incorrect
        else:
            print(f"incorrect !! ❌|❌|correct {rounds_won}| incorrect {rounds_lost + 1}")
            print("==========================================")
            rounds_lost += 1

        # once the user reaches desired amount of rounds, ask if they want to continue.
        if rounds_played == rounds:
            play_again = choice_checker(f"you've played {rounds} rounds |"
                                        f" would you like to continue?", yes_no_list, "please enter yes or no")
            # if yes, every 10 rounds ask if they wish to
            if play_again == "yes":
                if rounds_played == rounds + 10:
                    play_again()
                    continue

            # once user reaches desired amount of rounds, display choice whether
            # they want to level up to higher difficulty or end game.
            else:
                level_up = choice_checker(
                    f"would you like to level up to medium or hard difficulty?",
                    yes_no_list, "please enter yes or no")

                # if yes, give the option to level up
                if level_up == "yes":
                    dif_change = choice_checker("~ medium or hard ~", dif_list[:-1],
                                                "please enter medium or hard")

                # ends game if user decides not to level up
                else:
                    print()
                    print("you chose not to level up | Bye bye!👋👋")
                    end_game = "yes"
                    break
