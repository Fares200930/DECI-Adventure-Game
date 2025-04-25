import time
import random
import json

def print_pause(message, delay=1):
    """Print a message with a delay."""
    print(message)
    time.sleep(delay)

def intro():
    """Introduce the game setting."""
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a dangerous creature is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("To your left is a dense forest.")
    print_pause("In your hand you hold your trusty (but not very effective) rusty old magic wand.")

def cave(items):
    """Handle the cave scenario."""
    if "magic wand" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and there's nothing left to take.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Wand of Ogoroth!")
        print_pause("You discard your rusty old magic wand and take the Wand of Ogoroth with you.")
        items.append("magic wand")
    print_pause("You walk back out to the field.")

def forest(items):
    """Handle the forest scenario."""
    print_pause("You venture into the dense forest.")
    if "healing potion" in items:
        print_pause("You find nothing new here. The forest is quiet.")
    else:
        print_pause("You find a healing potion hidden under a bush!")
        items.append("healing potion")
    print_pause("You walk back out to the field.")

def house(items, health):
    """Handle the house scenario."""
    creatures = ["dragon", "goblin", "troll", "wicked fairy", "gorgon"]
    creature = random.choice(creatures)
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps a {creature}.")
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} attacks you!")
    if "magic wand" in items:
        combat(creature, items, health)
    else:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.")
        combat(creature, items, health)

def combat(creature, items, health):
    """Handle combat with a creature."""
    while True:
        print_pause(f"Your current health: {health['hp']}")
        action = input("Would you like to (1) cast a spell or (2) run away?\n")
        if action == "1":
            if "magic wand" in items:
                print_pause(f"As the {creature} moves to attack, you raise your Wand of Ogoroth.")
                print_pause("The Wand of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
                print_pause(f"But the {creature} takes one look at your shiny new wand and runs away!")
                print_pause(f"You have rid the town of the {creature}. You are victorious!")
                play_again()
            else:
                print_pause(f"You do your best, but your rusty old magic wand is no match for the {creature}.")
                health["hp"] -= 10
                if health["hp"] <= 0:
                    print_pause("You have been defeated!")
                    play_again()
        elif action == "2":
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
            break
        else:
            print_pause("Sorry, I don't understand that.")

def save_game(items, health):
    """Save the game state to a file."""
    with open("save_game.json", "w") as save_file:
        json.dump({"items": items, "health": health}, save_file)
    print_pause("Game saved!")

def load_game():
    """Load the game state from a file."""
    try:
        with open("save_game.json", "r") as save_file:
            data = json.load(save_file)
            print_pause("Game loaded!")
            return data["items"], data["health"]
    except FileNotFoundError:
        print_pause("No saved game found. Starting a new game.")
        return [], {"hp": 100}

def play_again():
    """Ask the player if they want to play again."""
    response = input("Would you like to play again? (y/n)\n").lower()
    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()

def play_game():
    """Start the game."""
    items, health = load_game()
    intro()
    while True:
        print_pause("\nEnter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("Enter 3 to explore the forest.")
        print_pause("Enter 4 to save your game.")
        print_pause("What would you like to do?")
        choice = input("(Please enter 1, 2, 3, or 4.)\n")
        if choice == "1":
            house(items, health)
        elif choice == "2":
            cave(items)
        elif choice == "3":
            forest(items)
        elif choice == "4":
            save_game(items, health)
        else:
            print_pause("Sorry, I don't understand that.")

# Run the game
if __name__ == "__main__":
    play_game()