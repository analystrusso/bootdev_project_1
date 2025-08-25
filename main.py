from character import player, create_character
from dialogue import load_dialogue, traverse_dialogue
from world import road_west
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


    # Commands
    if choice == "character":
        create_character(player)
    if choice == "inventory":
        print(player.inventory)

    interaction_handled = False
    dialogue_nodes = load_dialogue("dialogue.json")

    for npc in location.friendlies:
        if choice == "hello":
            start_key = f"{npc.job.lower()}_start"
            if start_key in dialogue_nodes:
                start_node = dialogue_nodes[start_key]
                traverse_dialogue(start_node)
                interaction_handled = True
            else:
                print(f"{npc.name} doesn't seem to want to talk right now.")
            break

    if not interaction_handled:
        try:
            if choice in location.connections:
                location = location.connections[choice]
            else:
                print("You cannot go that way.")
        except ValueError:
            print("invalid choice")