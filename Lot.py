import random
from time import sleep


def lot():
    print("Starting Draw Program")
    options = []
    user_input = input("enter the number of options you want to to make the lot\n")
    user_input = int(user_input)

    for i in range(user_input):
        user_options = input("Please enter the " + str(i + 1) + " option\n" + str(i + 1) + "." + "  ")
        options.append(user_options)
        with open('data.txt', 'w+') as nf:
            nf.write('\n'.join(options))
    print("\n")
    sleep(3)
    print(random.choice(options))


lot()
