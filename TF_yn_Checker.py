def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print(" Programme continues")
            print()

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:

            print()
            print("**please answer yes or no**")
            print()


def instructions():
    print("instructions")


print()
played_before = yes_no("Have you played the game before?")

if played_before == "no":
    instructions()
