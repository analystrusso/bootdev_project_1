def basic_convo(npc):
    print(f"{npc.name} says: Hello good traveller!")

    while True:
        prompts = {
            "1": "Good day. Do you think we'll have good weather for hunting?",
            "2": "I'm here to do some shopping.",
            "3": "Hello. I'm just passing by; don't mind me."
        }

        responses = {
            "1": "I hear the weather is going to be sunny today.",
            "2": "I have some interesting things to trade. Want to see?",
            "3": "Not a problem. Good day to you!"
        }

        print("\nOptions:")
        for key, text in prompts.items():
            print(f"{key}. {text}")

        choice = input("\nChoose an option:")

        if choice in responses:
            print(responses[choice])
            if choice == "3":
                break
        else:
            print("I don't understand.")


