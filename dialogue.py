class DialogueNode:
    def __init__(self, npc_line):
        self.npc_line = npc_line
        self.choices = {}  # {player_choice: DialogueNode}

# Nodes
start = DialogueNode("Hello traveler, what brings you here?")
weather = DialogueNode("The weather looks fine today!")
news = DialogueNode("What's new in the world?")
oh_really = DialogueNode("Oh really? I didn't expect that to happen!")
shop = DialogueNode("Here are my wares.")
goodbye = DialogueNode("Farewell!")

# Edges
start.choices = {
    "Ask about the weather.": weather,
    "Show me what you have for sale.": shop,
    "What's new?": news,
    "Goodbye.": goodbye
}
weather.choices = {
    "Back to start.": start,
    "Goodbye.": goodbye
}
shop.choices = {
    "Back to start.": start,
    "Goodbye.": goodbye
}
news.choices = {
    "Back to start.": start,
    "Oh really?": oh_really,
    "Goodbye.": goodbye
}
oh_really.choices = {
    "Goodbye.": goodbye
}

def traverse_dialogue(start_node):
    current = start_node
    while True:
        print("\nNPC:", current.npc_line) # Print NPC line

        if not current.choices:
            print("\n--- End of conversation ---") # If no choices, end convo
            break

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
        current = current.choices[chosen_text]
