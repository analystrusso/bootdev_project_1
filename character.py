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
