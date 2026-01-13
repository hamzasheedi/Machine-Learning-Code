import random

def guess_game(number):
    while True:
        try:
            user_input = int(input("Enter your guess (1-10): "))

            if user_input < 1 or user_input > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if user_input == number:
                print("You win!")
                break
            elif user_input > number:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")

        except ValueError:
            print("Only integers are allowed!")
            choice = input("Type 'exit' to quit or press Enter to continue: ")
            if choice.lower() == "exit":
                print(f"The correct number was {number}.")
                break

number = random.randint(1, 10)
guess_game(number)
