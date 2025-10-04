import random ##Importing random numbers using the random function.##

def Game_Replay():
    print("Welcome to the number guessing game!. You have 7 tries to get it right.\n Let's begin.") ##Intro to the game.##
##Establishing a Range that the user can define at the start of the game.##
Low_Number = int(input("Please enter the starting range number: "))
High_Number = int(input("Please enter the ending range number: "))

print("you have 7 tries to get the number between", Low_Number, "and", High_Number, "don't get caught out!")

number = random.randint(Low_Number, High_Number)
Tries = 7
Guess_counter = 0

while Guess_counter < Tries:
    guess = int(input("Guess a number: "))
    Guess_counter +=1
    if guess == number:
        print("You got it!", number, ", you guessed it in, ", Guess_counter, ".")
        break
    elif Guess_counter >= Tries and guess != number:
        print("Sorry it was, ", number, "Try again")

    elif guess > number:
        print("Too high, think of a lower number.")

    elif guess < number:
        print("Too low, think of a higher number.")

while True:
    Game_Replay()
    Restart = input("Do you want to restart? (yes/no): ").strip().lower()
    if Restart not in ('yes', 'y', 'Yes'):
        print("Thank you for playing!")
        break

