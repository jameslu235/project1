import random

# Ask the user for an upper limit
upper_limit = input("Enter a number: ")

# Validate the input
if upper_limit.isdigit():
    upper_limit = int(upper_limit)
    if upper_limit <= 0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Invalid input. Please enter a number.")
    quit()

# Generate a random number within the specified range
target_number = random.randint(0, upper_limit)
attempts = 0

# Start the guessing loop
while True:
    attempts += 1
    guess = input("Enter your guess: ")

    # Validate the user's guess
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid input. Please enter a number.")
        continue

    # Check the guess
    if guess == target_number:
        print("Congratulations! You guessed it right!")
        break
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

# Display the total number of attempts
print(f"You guessed it in {attempts} tries!")
