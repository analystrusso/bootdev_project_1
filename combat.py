import random
from dataclasses import dataclass, field

@dataclass
class Combatants:
    name: str
    type: str
    init: int = 0


def get_initiative(num_sides=20):
    for i in range(1, num_sides):
        return i

def set_initiative_order(combatants):
    for combatant in combatants:
        combatant.initiative = get_initiative()
        return sorted(combatants, key=lambda c: c.initiative, reverse=True)

