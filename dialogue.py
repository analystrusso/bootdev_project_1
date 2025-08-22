class DialogueNode:
    def __init__(self, npc_line, end_conversation=False):
        self.npc_line = npc_line
        self.choices = {}  # {player_choice: DialogueNode}
        self.end_conversation = end_conversation

# Shared nodes
goodbye = DialogueNode("Farewell!", end_conversation=True)

# Bakery start
baker_start = DialogueNode("Good day, traveler, welcome to the bakery. How are you today?")
baker_start.choices = {
    "What's fresh?": DialogueNode("I've got some wonderful sourdough in the oven, and rye in the display case. Care to try some?"),
    "I'm well, but I actually have to get going now.": goodbye
}

# Bakery first level
baker_fresh = baker_start.choices["What's fresh?"]
baker_fresh.choices = {
    "Certainly. Let's try the sourdough, please.": DialogueNode("There you are; what do you think of it?"),
    "No thanks, but it smells delicious.": DialogueNode("No problem. I'll see you later, I suppose."),
    "I'd love to, but I'm afraid I'm allergic to sourdough.": goodbye
}

# Bakery second level
baker_sourdough = baker_fresh.choices["Certainly. Let's try the sourdough, please."]
baker_sourdough.choices = {
    "The crust is really crisp. I like it!": DialogueNode("I'm very pleased to hear that, thank you."),
    "It's not exactly to my taste. Can I try some of the rye instead?": DialogueNode("Sure. I'm particularly proud of this one."),
    "Actually, I've just remembered an important appointment and need to run. Ta!": goodbye
}



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
