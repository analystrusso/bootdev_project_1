from dataclasses import dataclass, field

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
village_street = Location(
    "village street",
    "the main dirt road",
    "The village’s main street, lined with timber cottages, small gardens,\n "
    "and fenced farmyards. Chickens scratch in the dust and smoke rises from chimneys."
)

village_green = Location(
    "village green",
    "a small open green",
    "A grassy commons at the center of the village, used for gatherings and \nmarkets. "
    "Children play here while elders gossip nearby."
)

church = Location(
    "parish church",
    "a small wooden church",
    "A wooden church with a simple bell tower. Its doorway is decorated with \ncarved saints, "
    "and villagers gather here on holy days."
)

tavern = Location(
    "inn and tavern",
    "a lively tavern",
    "The tavern smells of ale and smoke. Travelers and locals alike gather here \nto drink, "
    "share news, and strike bargains."
)

smithy = Location(
    "blacksmith's forge",
    "a smoky forge",
    "The air is filled with the ringing of hammer on anvil. Tools, horseshoes, and \nweapons "
    "line the walls of the smithy."
)

manor = Location(
    "manor house",
    "the lord’s manor",
    "A timber-and-stone manor overlooking the village. Barns, stables, and a small \norchard "
    "surround the lord’s house. Peasants come here to render dues."
)

farmland = Location(
    "open fields",
    "strip fields of rye and oats",
    "Long, narrow strips of farmland stretch across the plain. The three-field rotation \nis "
    "clear: two parts for spring and autumn planting, and the third part left fallow."
)

meadow = Location(
    "meadow",
    "a grassy meadow",
    "A wide meadow near the stream, filled with tall grasses and wildflowers. "
    "Cattle and sheep graze under the watch of a herdsman."
)

stream = Location(
    "stream crossing",
    "a shallow stream with a mill",
    "A clear stream winds past the village. A wooden bridge spans it, and the watermill "
    "turns slowly nearby, grinding grain for bread."
)

forest_outskirts = Location(
    "forest edge",
    "the edge of the forest",
    "The first trees of the great forest rise here. Paths lead into the shadows,\n "
    "where game and danger both lurk."
)

# Link locations
village_street.connections = {"north": village_green, "south": farmland, "east": tavern, "west": smithy}
village_green.connections = {"south": village_street, "north": church, "east": manor}
church.connections = {"south": village_green}
tavern.connections = {"west": village_street}
smithy.connections = {"east": village_street}
manor.connections = {"west": village_green}
farmland.connections = {"north": village_street, "south": meadow}
meadow.connections = {"north": farmland, "east": stream}
stream.connections = {"west": meadow, "east": forest_outskirts}
forest_outskirts.connections = {"west": stream}
