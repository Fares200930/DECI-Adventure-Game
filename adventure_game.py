"""Module providing a function printing python version."""
import time
import random

# Creature power levels and scores
CREATURES = {
    "shadow wolf": {"power": 10, "score": 50},
    "fire imp": {"power": 5, "score": 20},
    "rock titan": {"power": 7, "score": 30},
    "spectral witch": {"power": 4, "score": 15},
    "poison viper": {"power": 8, "score": 40},
}

# Tool power levels
TOOLS = {
    "cracked wand": 2,
    "wand of radiance": 10,
    "steel sword": 6,
    "obsidian blade": 12,
}


def print_pause(message):
    """Print a message with a delay."""
    print(message)
    time.sleep(2)


def get_valid_input(prompt, options):
    """Prompt the user until a valid input is received."""
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print_pause("Invalid choice. Please try again.")


def cave(items):
    """Handle the cave scenario with random events."""
    print_pause("You peer cautiously into the cave.")
    if "wand of radiance" in items or "obsidian blade" in items:
        print_pause(
            "You've been here before, and gotten all the good stuff. "
            "It's just an empty cave now."
        )
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the legendary Wand of Radiance!")
        if "cracked wand" in items:
            print_pause(
                "You discard your cracked wand and take the Wand of Radiance "
                "with you."
            )
            items.remove("cracked wand")
        items.append("wand of radiance")
        print_pause("Wand of Radiance has been added to the backpack.")
    print_pause("You walk back out to the field.")


def house(items, health, total_score, current_creature):
    """Handle the house scenario."""
    if not current_creature:
        current_creature = random.choice(list(CREATURES.keys()))

    creature = current_creature
    print_pause("You approach the door of the house.")
    print_pause(
        (
            f"You are about to knock when the door opens and out steps a "
            f"{creature}."
        )
    )
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} finds you!")
    print_pause("You feel a bit under-prepared for this.")

    action = get_valid_input(
        "Would you like to (1) fight or (2) run away?\n", ["1", "2"]
    )
    if action == "1":
        chosen_item = backpack(items)
        player_power = TOOLS.get(chosen_item, 0)

        if player_power >= CREATURES[creature]["power"]:
            print_pause(
                f"As the {creature} moves to attack, you raise your "
                f"{chosen_item}."
            )
            if "wand of radiance" in items:
                print_pause(
                    f"The {chosen_item} shines brightly in your hand as "
                    "you brace yourself."
                )
            else:
                print_pause(
                    (
                        f"But the {creature} takes one look at your shiny new "
                        "wand and runs away!"
                    )
                )
            total_score += CREATURES[creature]["score"]
            print_pause(
                f"You have rid the town of the {creature}. You are victorious!"
            )
            print_pause(f"Your score is now {total_score}.")

            response = get_valid_input(
                "Would you like to play again? (Y/n)\n", ["y", "n"]
            )
            if response == "y":
                print_pause("Restarting the game while saving your score...")
                play_game(total_score)
            else:
                print_pause(
                    f"Thanks for playing! Your final score was "
                    f"{total_score}. Goodbye!"
                )
                exit()
        else:
            print_pause(
                f"You do your best, but your "
                f"{chosen_item} is no match for the {creature}."
            )
            health["hp"] -= 20
            print_pause(
                f"The {creature} attacks you! Your health is now "
                f"{health['hp']}."
            )
            if health["hp"] <= 0:
                print_pause("You have been defeated!")
                play_again(total_score)
            else:
                print_pause("You manage to escape back into the field.")
    elif action == "2":
        print_pause(
            "You run back into the field. Luckily, you don't seem to have "
            "been followed."
        )
    return current_creature, total_score


def forest(items):
    """Handle the forest scenario with random events."""
    print_pause("You venture into the dense forest.")
    events = [
        "You find a healing potion hidden under a bush!",
        "You encounter a friendly sprite who gives you a glowing amulet!",
        "You stumble upon a treasure chest filled with golden coins!",
        "You find a steel sword lying on the ground!",
        "You hear strange noises but find nothing unusual.",
    ]
    event = random.choice(events)
    print_pause(event)

    if "healing potion" not in items and "potion" in event:
        items.append("healing potion")
        print_pause("Healing Potion has been added to the backpack.")
    elif "glowing amulet" in event:
        items.append("glowing amulet")
        print_pause("Glowing Amulet has been added to the backpack.")
    elif "golden coins" in event:
        items.append("golden coins")
        print_pause("Golden Coins have been added to the backpack.")
    elif "steel sword" in event:
        if "cracked wand" in items:
            print_pause(
                "You discard your cracked wand and take the steel sword "
                "with you."
            )
            items.remove("cracked wand")
        items.append("steel sword")
        print_pause("Steel Sword has been added to the backpack.")
    print_pause("You walk back out to the field.")


def backpack(items):
    """Display the player's backpack and allow them to choose an item."""
    print_pause("You open your backpack and see the following items:")
    for i, item in enumerate(items, start=1):
        power = TOOLS.get(item, 0)
        print_pause(
            f"{i}. {item} "
            f"(Power: {power})"
        )

    while True:
        choice = get_valid_input(
            "Choose an item by number:\n",
            [str(i) for i in range(1, len(items) + 1)]
        )
        chosen_item = items[int(choice) - 1]
        print_pause(
            f"You have chosen the {chosen_item} "
            f"(Power: {TOOLS[chosen_item]})."
        )
        return chosen_item


def play_again(total_score):
    """Prompt the player to play again or exit."""
    response = get_valid_input(
        "Would you like to play again? (yes/no)\n", ["yes", "no"]
    )
    if response == "yes":
        print_pause("Restarting the game...")
        play_game()
    else:
        print_pause(
            f"Thanks for playing! Your final score was "
            f"{total_score}. Goodbye!"
        )
        exit()


def play_game(total_score=0):
    """Start the game."""
    items = [
        "cracked wand"
    ]
    health = {"hp": 100}
    current_creature = None
    print_pause(
        "You find yourself standing in an open field, filled with grass and "
        "yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a dangerous creature is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty "
        "(but not very effective) cracked wand."
    )

    while total_score < 10:  # Game ends when the score reaches 10
        print_pause(f"Your current health: {health['hp']}")
        print_pause(f"Your current score: {total_score}")
        print_pause("\nEnter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("Enter 3 to explore the forest.")
        print_pause("Enter 4 to exit the game.")
        choice = get_valid_input(
            "(Please enter 1, 2, 3, or 4.)\n", ["1", "2", "3", "4"]
        )
        if choice == "1":
            current_creature, total_score = house(
                items, health, total_score, current_creature
            )
        elif choice == "2":
            cave(items)
        elif choice == "3":
            forest(items)
        elif choice == "4":
            print_pause("Thanks for playing! See you next time.")
            return  # Exit the game

    # After the loop ends, explain why the game ended
    if total_score >= 10:
        print_pause(
            "Congratulations! You won by reaching the target score of 10!"
        )
    else:
        print_pause("Game over. Better luck next time!")


if __name__ == "__main__":
    play_game()
