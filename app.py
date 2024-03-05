# A Sad Word Game.
# Imports
import sys

def get_validated_input(prompt, validation, error_message):
    """check valid input material."""
    while True:
        user_input = input(prompt).strip()
        if validation(user_input):
            return user_input
        else:
            print(error_message)

def get_name():
    """get user's name."""
    return get_validated_input(
        "What is your name? ",
        lambda name: len(name) > 0 and name.isalpha(),
        "Invalid name. Please enter a proper name."
    )

def get_age():
    age = get_validated_input(
        "What is your age? ",
        lambda age: age.isdigit() and int(age) >= 18,
        "Invalid age. You must be at least 18 years old."
    )
    return int(age)

def choose_destination(options):
    """pick destination for user."""
    print("Where do you want to go? Here are your options:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    choice = get_validated_input(
        "Choose an option (number): ",
        lambda x: x.isdigit() and 1 <= int(x) <= len(options),
        "Invalid choice. Please select a number from the list."
    )

    return options[int(choice) - 1]

def translate_to_pig_latin(word):
    """unnecessary pig latin for poops and giggles."""
    if word.isalpha():
        return word[1:].lower() + word[0].lower() + 'ay'
    else:
        return None

def main():
    print("Welcome to the Adventure Game. Life is full of surprises.")
    
    name = get_name()
    print(f"Hello, {name}, let's embark on this journey together.")
    
    age = get_age()
    print(f"Great, {name}. At {age} years old, you're ready for this adventure.")
    
    destinations = ["the mystical forest", "the ancient castle", "the mysterious cave"]
    first_destination = choose_destination(destinations)
    print(f"{name}, you're heading to {first_destination}. Exciting!")

    second_destination = choose_destination(destinations)
    print(f"Next, we're off to {second_destination}. Adventure awaits!")

    word = get_validated_input(
        "Enter a word to translate to Pig Latin: ",
        lambda x: x.isalpha(),
        "Invalid word. Please enter a single word without spaces or numbers."
    )
    pig_latin_word = translate_to_pig_latin(word)
    print(f"The Pig Latin translation is: {pig_latin_word}")

    print("Now, as we conclude our journey, reflect on the paths taken and the choices made.")

# Run game    
if __name__ == "__main__":
    main()
