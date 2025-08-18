from world import Location, village
from character import Character, hero_1, hero_2, hero_3

running = True

# Character select
heroes = {
    "adelbert": hero_3,
    "doric": hero_1,
    "erzsebet": hero_2
}

# Print hero choices
print("choose your hero:")
for hero_obj in heroes.values():
    print(f"- {hero_obj.name} ({hero_obj.job})")

# Let the player choose
choice = input("> ").lower()

if choice in heroes:
    current_hero = heroes[choice]
    print(f"You have chosen {current_hero.name}, the {current_hero.job}")
else:
    print("Invalid choice, try again.")


# Game loop and traversal
current_location = village
print(current_location.description)

while running:
    print(f"\nYou are at the {current_location.name}: {current_location.description}\n")

    for direction, destination in current_location.connections.items():
        print(f"- {direction} to {destination.truncated_description}")
    print("Where would you like to go?")

    choice = input("> ").lower()

    try:
        if choice in current_location.connections:
            current = current_location.connections[choice]
            print(current.description)
        else:
            print("You cannot go that way.")
    except ValueError:
        print("invalid choice")