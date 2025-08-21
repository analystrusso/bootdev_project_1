from dataclasses import dataclass
from world import church, bakery, smithy, manor, village_green, tavern, farmland


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
church.friendlies.append(priest)

innkeeper = Friendlies(
    "Greta",
    "innkeeper",
    "tavern"
)
tavern.friendlies.append(innkeeper)

blacksmith = Friendlies(
    "Ulrich",
    "blacksmith",
    "smithy"
)
smithy.friendlies.append(blacksmith)
lord = Friendlies(
    "Lord Heinrich",
    "local lord",
    "manor"
)
manor.friendlies.append(lord)

farmer = Friendlies(
    "Brigid",
    "farmer",
    "farmland"
)
farmland.friendlies.append(farmer)

herbalist = Friendlies(
    "Anika",
    "herbalist",
    "village_green"
)
village_green.friendlies.append(herbalist)

baker = Friendlies(
    "Johann",
    "baker",
    "bakery"
)
bakery.friendlies.append(baker)