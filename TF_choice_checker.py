# True or False Choice checker testing v1


# Functions
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
yes_no_list = ["yes", "no"]
tf_list = ["true", "false", "tru", "xxx"]

answer = "true"

# loop for testing purpose
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker(" 3 * 4 = 12 (True or False?) ", tf_list,
                                 "please enter True or False")

    # print out choice for comparison purposes
    if user_choice == answer:
        print("You are correct")
    elif user_choice == "xxx":
        print("🐔🐔🐔🐔🐔")
        end_game = "yes"
        break
    else:
        print("You got it incorrect")
