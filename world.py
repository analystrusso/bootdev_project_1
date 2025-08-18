from dataclasses import dataclass, field
from enum import Enum

# Define game world -- done
# Define character
# Define enemies
# Define friendlies
# Define items


# def premise():
#    print("Premise: you are a hunter. You live in a village, and you've returned to "
#          "find it overrun with monsters.")

@dataclass
class Location:
    name: str
    truncated_description: str
    description: str
    connections: dict[str, "Location"] = field(default_factory=dict)
    enemies: list = field(default_factory=list)
    friendlies: list = field(default_factory=list)
    items: list = field(default_factory=list)

# Define locations
village = Location("village", "your village", "your home village")
farmland = Location("farmland", "farmers' fields", "farmland on the village outskirts")
meadow = Location("meadow", "a vast meadow", "wildflowers and tall grasses as far as you can see")
bridge = Location("bridge", "a stone bridge", "a small stone bridge over a stream. It marks the boundary between fields and forest.")
forest = Location("forest", "forest outskirts", "the paths here are well marked and the underbrush not too thick")

# Link locations
village.connections = {"north": farmland}
farmland.connections = {"south": village, "east": meadow, "north": bridge}
meadow.connections = {"west": farmland}
bridge.connections = {"south": farmland, "north": forest}
forest.connections = {"south": bridge}
