import random

def get_hint(secret, guess):

    diff = abs(secret - guess)

    if diff == 0:
        return None
    elif diff <= 5:
        direction = "higher" if secret > guess else "lower"
        return f"You're so close! Go a little {direction}."
    elif diff <= 15:
        direction = "higher" if secret > guess else "lower"
        return f" Try going {direction} please."
    
    elif diff <= 30:
        direction = "higher" if secret > guess else "lower"
        return f"Not quite. You're a bit {direction}."
    else:
        if secret > guess:
            return " Too low! Its Way higher than that."
        else:
            return "Too high! Way lower than that."

def play_game():
    max_guess = 7
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n")

    print("   NUMBER GUESSING GAME ")
    print("\n")
    
    print(f"A secret number between 1 and 100 is chosen, Guess what it is.")
    print("\n")

    print(f"You have {max_guess} guesses. Good luck!\n")
    print("\n")

    while attempts < max_guess:
        remaining = max_guess - attempts
        print(f"[Guess {attempts + 1}/{max_guess}] — {remaining} guess(es) remaining")

        try:
            user_guess = input("Your guess: ").strip()
            guess = int(user_guess)
        except ValueError:
            print("⚠️  Please enter a valid whole number.\n")
            continue

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.\n")
            continue

        attempts += 1

        if guess == secret_number:
            print("\n")
            print("🎉CONGRATULATIONS! You got it!")
            print(f"    The number was: {secret_number}")
            print(f"    You guessed it in {attempts} attempt(s).")
            print("\n")
            return

        hint = get_hint(secret_number, guess)
        print(f"   → {hint}\n")

    # Out of guesses
    print("\n")
    print("\n" + "=" * 45)
    print("GAME OVER! Out of guesses.")
    print(f"    The secret number was: {secret_number}")
    print(f"    You used all {max_guess} attempts.")
    print("=" * 45 + "\n")

def main():
    while True:
        play_game()
        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! See you next time. 👋\n")
            break

if __name__ == "__main__":
    main()