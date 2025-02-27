import random
import string
import math

def generate_password(length=12):
    if length < 6:
        return "Σφάλμα: Ο κωδικός πρόσβασης πρέπει να έχει τουλάχιστον 6 χαρακτήρες."
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def calculate_entropy(password):
    unique_characters = 0
    if any(c.islower() for c in password):
        unique_characters += 26
    if any(c.isupper() for c in password):
        unique_characters += 26
    if any(c.isdigit() for c in password):
        unique_characters += 10
    if any(c in string.punctuation for c in password):
        unique_characters += len(string.punctuation)
    entropy = math.log2(unique_characters ** len(password))
    return entropy

def assess_strength(entropy):
    if entropy < 40:
        return "Αδύναμος"
    elif entropy < 60:
        return "Μέτριος"
    else:
        return "Ισχυρός"

try:
    length = int(input("Εισαγάγετε το επιθυμητό μήκος κωδικού πρόσβασης (τουλάχιστον 6 χαρακτήρες): "))
    if length < 6:
        print("Σφάλμα: Το μήκος πρέπει να είναι τουλάχιστον 6 χαρακτήρες.")
    else:
        password = generate_password(length)
        entropy = calculate_entropy(password)
        strength = assess_strength(entropy)
        print("\nΔημιουργημένος κωδικός πρόσβασης:", password)
        print(f"Ισχύς κωδικού πρόσβασης: {strength}")
        print(f"Εντροπία: {entropy:.2f} bits")
except ValueError:
    print("Σφάλμα: Εισαγάγετε έναν έγκυρο αριθμό.")