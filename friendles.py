from dataclasses import dataclass

@dataclass
class Friendlies:
    name: str
    job: str
    location: str

# church tavern smithy manor farmland village_green

priest = Friendlies(
    "Father John",
    "village priest",
    "church"
)

innkeeper = Friendlies(
    "Greta",
    "innkeeper",
    "tavern"
)

blacksmith = Friendlies(
    "Ulrich",
    "blacksmith",
    "smithy"
)

lord = Friendlies(
    "Lord Heinrich",
    "local lord",
    "manor"
)

farmer = Friendlies(
    "Brigid",
    "farmer",
    "farmland"
)

herbalist = Friendlies(
    "Anika",
    "herbalist",
    "village_green"
)
