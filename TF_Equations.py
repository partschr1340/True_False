import random

while True:
    input()
    integer_1 = random.randint(1, 100)
    integer_2 = random.randint(1, 100)
    integer_3 = random.randint(1, 100)
    integer_4 = random.randint(1, 100)
    equation = random.randint(1, 100)

    if 0 < equation < 33:
        print(f"{integer_1} + {integer_2} = {integer_2 + integer_1}")
    elif 34 < equation < 66:
        print(f"{integer_3} - {integer_4} = {integer_3 - integer_4}")
    else:
        print(f"{random.randint(1,100)} + {random.randint(1,100)} > {random.randint(0,100)} + {random.randint(1,100)}")
