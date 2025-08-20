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

# === Locations ===
# Roads / entrances
road_west = Location("west road", "a dirt road leading west",
    "The road stretches westward, eventually reaching neighboring villages and fields."
)

village_entrance = Location("village entrance", "the main entrance into the village",
    "A stout wooden gate set in the palisade that circles the village. The road continues west."
)

road_east = Location("east road", "a dirt road leading east",
    "The road continues east toward the nearest town and market."
)

# Village street
village_street_west = Location("western end of main street", "the western part of the main dirt road",
    "The village’s main street, lined with timber cottages. The smithy lies to the north."
)

village_street = Location("main street", "the central part of the main dirt road",
    "The central part of the village's main street. Homes here are somewhat better appointed, "
    "and the nearby village green hosts frequent market days."
)

village_street_east = Location("eastern end of main street", "the eastern part of the main dirt road",
    "The main street’s eastern stretch, near the tavern and the road to the east."
)

village_street_south = Location("a well-worn cart path", "this path leads south from the village entrance",
                                "a well-worn cart path that leads south over the bridge to the mill.")

# Key village structures
bakery = Location("village bakery", "the bakery",
    "The smell of fresh bread wafts from the oven. Villagers come here daily for loaves."
)

smithy = Location("blacksmith's forge", "a smoky forge",
    "The air is filled with the ringing of hammer on anvil. Tools and horseshoes hang on the walls."
)

village_green = Location("village green", "a grassy commons",
    "A grassy open space used for gatherings, play, and small markets."
)

tavern = Location("inn and tavern", "a lively tavern",
    "The tavern smells of ale and smoke. Travelers and locals alike gather here to drink and share news."
)

church = Location("parish church", "a small wooden church",
    "A wooden church with a simple bell tower, decorated with carved saints. Villagers gather here on holy days."
)

manor = Location("manor house", "the lord’s manor",
    "A timber-and-stone manor overlooking the village. Barns, stables, and a small orchard surround it."
)

# Outskirts
farmland = Location("open fields", "strip fields of rye and oats",
    "Long, narrow strips of farmland stretch across the plain in rotation: spring, autumn, and fallow."
)

meadow = Location("meadow", "a grassy meadow",
    "A wide meadow near the stream, filled with tall grasses and wildflowers. Cattle graze here."
)

bridge = Location("stone bridge", "a small stone bridge",
    "A stout little bridge crossing the stream, marking the boundary between fields and woods."
)

mill = Location("watermill", "a watermill by the stream",
    "The wooden watermill creaks as the wheel turns. Grain is brought here for grinding."
)

# Lord’s woods
lords_woods = Location("lord’s woods", "the thick forest",
    "Tall oaks and beeches dominate this forest. It is the lord’s hunting preserve."
)

lords_woods_north = Location("lord’s woods - north", "the northern edge of the lord’s woods",
    "The northern reaches of the woods, not far from the manor."
)

lords_woods_south = Location("lord’s woods - south", "the southern edge of the lord’s woods",
    "The forest thins here, near a path leading back toward the stream."
)

lords_woods_west = Location("lord’s woods - west", "the western edge of the lord’s woods",
    "The woods are quieter here, further from the manor."
)

lords_woods_east = Location("lord’s woods - east", "the eastern edge of the lord’s woods",
    "The forest deepens here, with faint game trails leading further east."
)

# === Connections ===
# Roads and entrance
road_west.connections = {"east": village_entrance}
village_entrance.connections = {"west": road_west, "east": village_street_west, "north": bakery, "south": village_street_south}
road_east.connections = {"west": village_street_east}

# Main street
village_street_west.connections = {"west": village_entrance, "east": village_street, "north": smithy, "south": meadow}
village_street.connections = {"west": village_street_west, "east": village_street_east, "north": village_green, "south": church}
village_street_east.connections = {"west": village_street, "east": road_east, "north": tavern, "south": manor}

# Village structures
bakery.connections = {"south": village_entrance}
smithy.connections = {"south": village_street_west}
village_green.connections = {"south": village_street}
tavern.connections = {"south": village_street_east}
church.connections = {"north": village_street}
manor.connections = {"north": village_street_east, "east": lords_woods_north,
                     "south": lords_woods_west
                     }

# Outskirts
farmland.connections = {"north": road_west, "east": village_street_south, "south": bridge}
meadow.connections = {"west": village_street_south, "east": church}
bridge.connections = {"north": village_street_south, "south": mill}
mill.connections = {"north": bridge}

# Lord’s woods
lords_woods.connections = {"west": lords_woods_west,
                           "east": lords_woods_east,
                           "south": lords_woods_south,
                           }
lords_woods_north.connections = {"west": manor, "north": road_east}
lords_woods_west.connections = {"east": lords_woods, "north": manor}
lords_woods_east.connections = {"west": lords_woods}
lords_woods_south.connections = {"north": lords_woods}
