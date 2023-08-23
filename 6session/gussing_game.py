import random
low = 1
high = 100
turns = 0
number = random.randint(low,high)
ai_low = low
ai_high = high

print(number)

ai_guess = int((ai_high + ai_low) /2)
print(ai_guess)
guess = int(input(f"Guess a number between {low} and {high}: "))

while number != guess or number != ai_guess:
    if number == guess:
        print("Guessed right.")
    if number == ai_guess:
        print("AI guessed right.")

    if number < guess:
        print("Too High.")
        high = guess
    if number < ai_guess:
        print("Too High.")
        ai_high = ai_guess - 1

    if number > guess:
        print("Too low.")
        low = guess
    if number > ai_guess:
        print("Too low.")
        ai_low = ai_guess + 1
    
    ai_guess = int((ai_high + ai_low) /2)
    print(ai_guess)
    guess = int(input(f"Guess a number between {low} and {high}: "))