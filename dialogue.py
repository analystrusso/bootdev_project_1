import json
from pathlib import Path

class DialogueNode:
    def __init__(self, npc_line, end_conversation=False):
        self.npc_line = npc_line
        self.choices = {}  # {player_choice: DialogueNode}
        self.end_conversation = end_conversation

def load_dialogue(filename="dialogue.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Create all DialogueNode objects
    nodes = {}
    for node_name, node_data in data.items():
        nodes[node_name] = DialogueNode(
            node_data["npc_line"],
            node_data.get("end_conversation", False)
        )

    # Then wire up the choices
    for node_name, node_data in data.items():
        if "choices" in node_data:
            for choice_text, target_name in node_data["choices"].items():
                nodes[node_name].choices[choice_text] = nodes[target_name]
    return nodes


def traverse_dialogue(start_node):
    current = start_node
    while True:
        print("\nNPC:", current.npc_line) # Print NPC line

        if getattr(current, "end_conversation", False):
            print("\n--- Conversation ended ---")
            break

        if not current.choices:
            current = start_node
            continue

        # List available player choices
        choices_list = list(current.choices.keys())
        for i, choice in enumerate(choices_list, 1):
            print(f"{i}. {choice}")

        # Ask player for input
        while True:
            try:
                selection = int(input("Choose an option: "))
                if 1 <= selection <= len(choices_list):
                    break
                else:
                    print("Invalid selection; try again.")
            except ValueError:
                print("Please enter a number.")

        # Move to next node based on choice
        chosen_text = choices_list[selection - 1]
        next_node = current.choices[chosen_text]
        current = next_node

        if not current.choices and not getattr(next_node, "end_conversation", False):
            current = start_node
