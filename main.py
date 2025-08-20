from world import road_west
from character import choose_hero


# Define game world -- done for now
# Define character -- done for now
# Define enemies
# Define friendlies
# Define items
# Define combat -- initiative done

# def premise():
#    print("Premise: you are a hunter. You live in a village, and you've returned to "
#          "find it overrun with monsters.")


running = True
player = choose_hero()
location = road_west

while running:
    print(f"\nYou are at the {location.name}: {location.description}\n")

    for direction, destination in location.connections.items():
        print(f"- {direction} to {destination.truncated_description}")
    print("Where would you like to go?")

    choice = input("> ").lower()

    try:
        if choice in location.connections:
            location = location.connections[choice]
            # print(location.description)
        else:
            print("You cannot go that way.")
    except ValueError:
        print("invalid choice")