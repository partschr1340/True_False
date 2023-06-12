# Functions
print("=====WELCOME TO THE TRUE OR FALSE QUIZ =====")


# Instructions
def instructions():
    print("~~~~~~INSTRUCTIONS~~~~~~~")
    print("- You will choose your own difficulty (easy | medium | hard")
    print("- The difficulty you choose will influence the type of questions there are.")
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
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item),
        # the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)


def rounds_checker():
    while True:
        response = input("How many rounds would you like to play?")

        round_error = "Please enter an integer more than 0 or <enter> for infinite mode"

        # If infinite mode not chose, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue
        return response


# lists for checking responses
yes_no_list = ["yes", "no"]
tf_list = ["true", "false", "tru", "xxx"]
dif_list = ["easy", "medium", "hard"]

# Ask user if they have played game before, if yes continue, if no display instructions
print()
played_before = choice_checker("Have you played this game before?", yes_no_list, "~~Please enter yes or no~~")

if played_before == "no":
    instructions()

# What difficultly the user wants the question to be, ensures they enter valid difficulty
print()
print("Choose your difficulty:")
difficulty = choice_checker("====== easy | medium | hard ======", dif_list, "Please enter a valid difficulty")
print(f"\t======= {difficulty} mode =======")
print()
# Ask user how many rounds they wish to play at this difficulty
rounds_checker()

