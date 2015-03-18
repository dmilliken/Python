user_input = input("Give me a number: ")
num = int(user_input)

if num < 10 or num > 20:
    print("That\'s a good number")

if num > 10 and num < 20:
    print("You've found the sweet spot")