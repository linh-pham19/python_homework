def make_hangman(secret_word):
    guessed_letters = []
    def hangman_closure(letter):
        if type(letter) != str or len(letter) != 1:
            return "Please enter a single letter."
        if letter in guessed_letters:
            return "You already guessed that letter."
        guessed_letters.append(letter)
        display_word = ''.join(
            letter if letter in guessed_letters else '_' for letter in secret_word
        )
        if '_' not in display_word:
            return f"Congratulations! You've guessed the word: {secret_word}"
        return display_word
    return hangman_closure


hidden_secret = "closure"
game = make_hangman(hidden_secret)
has_won = False
tries = 0
while not has_won:
    user_guess = input("Type a single character guess for the hangman guess. ")
    while len(user_guess) > 1:
        user_guess = input("Invalid Input Error! Type a single character. ")
    tries += 1
    result = game(user_guess)
    if (hidden_secret in result): 
        has_won = True

print(f"You won in {tries} tries! The secret word was '{hidden_secret}'.")
print("Game Over!")

