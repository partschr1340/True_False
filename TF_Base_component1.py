# Online Python compiler (interpreter) to run Python online.# Functions
import random
import math


# Instructions
def instructions():
    print("~~~~~~INSTRUCTIONS~~~~~~~\n")
    print("- You will choose your own difficulty *easy | medium | hard*")
    print("- The difficulty you choose will influence the type of questions there are.")
    print("- You will then choose the amount of rounds you want to play at this difficulty or"
          " press <enter> for infinite mode.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("- Easy will include simple addition and subtraction.")
    print("- Medium will include some multiplication")
    print("- Hard will include very difficult division\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("- Equations will then be generated and you will have to find out if they are")
    print("  true or false\n")
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


# rounds component
def rounds_checker():
    while True:
        rounds_amount = input("How many rounds would you like to play? <enter for infinite rounds>")
        round_error = "Please enter an integer or press <enter> for infinite mode\n"

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
dif_list = ["hard", "medium", "easy"]
tf_error = "please enter true or false"
yes_no_error = "please enter yes or no"

# introduction message
print("\n➕➖✖➗ WELCOME TO THE TRUE OR FALSE QUIZ ➗✖➖➕\n")

# Ask user if they have played game before, if yes continue, if no display instructions
played_before = choice_checker("~~Do you know how the quiz works?", yes_no_list, "~~Please enter yes or no~~")

if played_before == "no":
    instructions()

# What difficultly the user wants the question to be, ensures they enter valid difficulty
print()
print("Choose your difficulty:")
difficulty = choice_checker("====== easy (➕➖) | medium (✖) | hard (➗) ======", dif_list,
                            "\nPlease enter a valid difficulty")
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

# in game messages
end_game_message = "You got {} correct✅✅ | You also got {} incorrect❌❌\n"
play_again = f"you've played {rounds} rounds would you like to continue?\n"
incorrect = "incorrect !! ❌❌|correct {}| incorrect {}\n"
correct = "you got it, nice! 👍👍| correct {}| incorrect {}"

# states how many rounds the user has chosen
print(f"{rounds} rounds | {mode} mode")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

end_game = "no"
# easy mode
if difficulty == "easy":

    while True:
        # random integers for equation generators
        integer_1 = (random.randint(50, 100))
        integer_2 = (random.randint(50, 100))
        # randomizes questions so that it spread equally ( +, -, <, >)
        randomizer = random.randint(1, 60)

        # ensures that equations are randomized via true or false equations
        equation = random.choice(tf_list[:-1])
        response = tf_list

        # displays true equations randomly
        if equation == "true":
            if 1 < randomizer < 20:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_1} + {integer_2} ={integer_1 + integer_2}"
                    f" (spoiler True) | True or False?", tf_list, tf_error)

                rounds_played += 1

            elif 21 < randomizer < 40:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_1} - {integer_2} ={integer_1 - integer_2} "
                    f"(spoiler True) | True or False?", tf_list, tf_error)
                rounds_played += 1

            else:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_1} + {integer_2} > {random.randint(25, 49)} + {random.randint(25, 49)} "
                    f"(spoiler True) | True or false?", tf_list, tf_error)
                rounds_played += 1

        # displays false equations randomly
        elif equation == "false":
            if 1 < randomizer < 20:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} |"
                    f" {integer_1} + {integer_2} ={random.randint(0, 49)} (spoiler {equation})"
                    f"| True or False?", tf_list, tf_error)
                rounds_played += 1

            elif 21 < randomizer < 40:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} | "
                    f"{integer_1} - {integer_2} ={74, 255} (spoiler {equation})"
                    f"| True or False?", tf_list, tf_error)
                rounds_played += 1

            else:
                user_choice = choice_checker(
                    f"round {rounds_played + 1} | "
                    f"{integer_2} + {integer_1} < {random.randint(20, 44)} + {random.randint(19, 58)}"
                    f" (spoiler {equation})"
                    f"| True or False?", tf_list, tf_error)
                rounds_played += 1

        # displays a message if user got it right
        if user_choice == equation:
            print(correct.format(rounds_won + 1, rounds_lost + 1))
            print("==========================================\n")
            rounds_won += 1

        # end game code, only display chicken if user decided to end game on regular mode
        elif user_choice == "xxx":
            if mode == "infinite":
                if rounds_played == 0:
                    print("~ Bye bye!")
                    end_game = "yes"
                    break
                else:
                    print("\n==========================================")
                    print(end_game_message.format(rounds_won, rounds_lost))
                    print("~Bye bye")
                    end_game = "yes"
                    break

            else:
                print("🐔🐔🐔You chickened out!!🐔🐔🐔\n")
                print("==========================================\n")
                print(end_game_message.format(rounds_won, rounds_lost))
                end_game = "yes"
                break

        # displays an incorrect message if user gets it incorrect
        else:
            print("incorrect !! ❌❌|correct {}| incorrect {}\n")
            print("==========================================\n")
            rounds_lost += 1
            continue

        # once the user reaches desired amount of rounds, ask if they want to continue.
        if rounds_played == rounds:
            play_again = choice_checker(play_again, yes_no_list, yes_no_error)
            # if yes, every 10 rounds ask if they wish to
            if play_again == "yes":
                mode = "infinite"
                continue
            else:
                print(end_game_message.format(rounds_won, rounds_lost))
                end_game = "yes"
                break

# Medium difficulty
if difficulty == "medium":
    while True:
        # Random integers for equations
        int_1 = random.randint(30, 80)
        int_2 = random.randint(15, 30)

        # randomizes whether equation printed is a true or false equation
        equation = random.choice(tf_list[:-1])

        # displays true multiplication equations
        if equation == "true":
            user_choice = choice_checker(f"round {rounds_played + 1} |"
                                         f"{int_1} x {int_2} = {int_2 * int_1}"
                                         f" | True or False? (spoiler True)", tf_list, tf_error)
            rounds_played += 1

        # prints random false multiplication equation
        else:
            user_choice = choice_checker(f"round {rounds_played + 1} |"
                                         f"{int_1} x {int_2} = {random.randint(30, 50) ** 2}"
                                         f" | True or False (spoiler False)", tf_list, tf_error)
            rounds_played += 1

        # print correct message if user gets answer correct
        if user_choice == equation:
            print(correct.format(rounds_won + 1, rounds_lost))
            print("==========================================\n")
            rounds_won += 1

        # ends the game if user types xxx (only displays chicken if user ends game without
        # infinite rounds
        elif user_choice == "xxx":
            if mode == "infinite":
                print("\n==========================================")
                print(end_game_message.format(rounds_won, rounds_lost))
            else:
                print("\n==========================================")
                print("🐔🐔🐔You chickened out!!!🐔🐔🐔")
                print(end_game_message.format(rounds_won, rounds_lost))
            end_game = "yes"
            break

        # displays incorrect message
        else:
            print(incorrect.format(rounds_won, rounds_lost + 1))
            print("==========================================\n")
            rounds_lost += 1
        # ends game if user does not wish to play again
        if rounds_played == rounds:
            play_again = choice_checker(play_again, yes_no_list, yes_no_error)
            if play_again == "yes":
                mode = "infinite"
                continue
            else:
                print("\n", end_game_message.format(rounds_won, rounds_lost))
                print("~bye bye")
                end_game = "yes"
                break

# Hard difficulty
if difficulty == "hard":
    while True:
        # integers for hard division questions
        div_1 = random.randint(90, 2502)
        div_2 = random.randint(9, 15)

        # randomizes whether the equation is true or false
        equation = random.choice(tf_list[:-1])

        # True division equation ( searched google to round to 2dp)
        if equation == "true":
            user_choice = choice_checker(f"round {rounds_played + 1} |"
                                         f"{div_1} / {div_2} = {div_1 / div_2:.2f}"
                                         f" | True or False (spoiler {equation})", tf_list, tf_error)
            rounds_played += 1

        # False division equation ( used square root to display a false integer,
        # which was searched using google)
        if equation == "false":
            user_choice = choice_checker(f"round {rounds_played + 1} |"
                                         f"{div_1} / {div_2} = {math.sqrt(div_1):.2f}"
                                         f" | True or False (spoiler False)", tf_list, tf_error)
            rounds_played += 1

        # displays correct message
        if user_choice == equation:
            print(correct.format(rounds_won + 1, rounds_lost))
            print("==========================================\n")
            rounds_won += 1

        # ends game if user types in exit game code
        elif user_choice == "xxx":
            if mode == "infinite":
                print("\n==========================================")
                print(end_game_message.format(rounds_won, rounds_lost))
            else:
                print("\n==========================================")
                print("🐔🐔🐔")
                print(end_game_message.format(rounds_won, rounds_lost))

            end_game = "yes"
            break

        # displays incorrect message
        else:
            print(incorrect.format(rounds_won, rounds_lost + 1))
            print("==========================================\n")
            rounds_lost += 1

        # ends game if user does not wish to play again, if they do, continue to infinite mode.
        if rounds_played == rounds:
            play_again = choice_checker(play_again, yes_no_list, yes_no_error)
            if play_again == "yes":
                mode = "infinite"
                rounds = "unlimited"
                continue
            else:
                print("\n", end_game_message.format(rounds_won, rounds_lost))
                print("~bye bye")
                end_game = "yes"
                break

print("🐒🐒🐒🐒🐒🐒🐒🐒🐒\nThanks for playing\n🐒🐒🐒🐒🐒🐒🐒🐒🐒")
