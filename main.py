from world import Location, village
from character import Character

running = True
current = village
print(current.description)

while running:
    print(f"\nYou are at the {current.name}: {current.description}\n")

    for direction, destination in current.connections.items():
        print(f"- {direction} to {destination.truncated_description}")
    print("Where would you like to go?")

    choice = input("> ").lower()

    try:
        if choice in current.connections:
            current = current.connections[choice]
            print(current.description)
        else:
            print("You cannot go that way.")
    except ValueError:
        print("invalid choice")