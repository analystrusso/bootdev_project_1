from dataclasses import dataclass, field

@dataclass
class Character:
    name: str
    description: str
    job: str
    inventory: list = field(default_factory=list)
    weapons: list = field(default_factory=list)
    spells: list = field(default_factory=list)

hero_1 = Character(
    name="Doric",
    description="a ranger",
    job="ranger"
)

hero_2 = Character(
    name="Erzsebet",
    description="a witch",
    job="witch"
)

hero_3 = Character(
    name="Adelbert",
    description="a warrior",
    job="warrior"
)

heroes = {
    "doric": hero_1,
    "erszebet": hero_2,
    "adelbert": hero_3
}

def choose_hero():
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