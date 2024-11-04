import random

flag = True
while flag:
    command = input()
    if (command == "Hi"):
        print("Hi")
    elif (command == "GetRandom"):
        print(random.randint(1, 10000))
    elif (command == "Shutdown"):
        flag = False
