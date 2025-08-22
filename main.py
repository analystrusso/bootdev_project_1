from world import road_west
from character import choose_hero
from dialogue import traverse_dialogue, baker_start
import friendlies

# Define game world -- done for now
# Define character -- done for now
# Define enemies -- working on it
# Define friendlies -- done for now
# Define dialogue -- working on it
# Define items -- working on it
# Define combat -- initiative done
# Define trade -- working on it

# def premise():
#    print("Premise: you are a hunter. You live in a village, and you've returned to "
#          "find it overrun with monsters.")

running = True
player = choose_hero()
location = road_west

while running:
    print(f"\nYou are at the {location.name}: {location.description}\n")

    print("You see:")
    for npc in location.friendlies:
        print(f"- {npc.name}, the {npc.job}")

    for direction, destination in location.connections.items():
        print(f"- {direction} to {destination.truncated_description}")
    print("Where would you like to go?")

    choice = input("> ").lower()
    interaction_handled = False

    for npc in location.friendlies:
        if choice == "hello":
            traverse_dialogue(baker_start)
            interaction_handled = True
            break

    if not interaction_handled:
        try:
            if choice in location.connections:
                location = location.connections[choice]
            else:
                print("You cannot go that way.")
        except ValueError:
            print("invalid choice")