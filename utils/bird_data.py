bird_database = {
    "peacock": {
        "scientific_name": "Pavo cristatus",
        "description": "A colourful bird famous for its spectacular feather display.",
        "habitat": "Forests, grasslands and agricultural areas",
        "diet": "Seeds, insects, fruits and small reptiles",
        "lifespan": "15–20 years",
        "facts": [
            "It is the national bird of India.",
            "Male peafowls are called peacocks.",
            "Its colourful train is used during courtship."
        ]
    },

    "parrot": {
        "scientific_name": "Psittacula krameri",
        "description": "An intelligent bird known for its curved beak and ability to imitate sounds.",
        "habitat": "Forests, woodlands and urban areas",
        "diet": "Fruits, seeds, nuts and flowers",
        "lifespan": "15–30 years",
        "facts": [
            "Parrots have strong curved beaks.",
            "They use their feet to hold food.",
            "Many species can imitate human speech."
        ]
    },

    "eagle": {
        "scientific_name": "Aquila",
        "description": "A powerful bird of prey with excellent eyesight.",
        "habitat": "Mountains, forests and open landscapes",
        "diet": "Fish, mammals and small animals",
        "lifespan": "20–30 years",
        "facts": [
            "Eagles have exceptional eyesight.",
            "They have powerful talons.",
            "They are skilled hunters."
        ]
    },

    "sparrow": {
        "scientific_name": "Passer domesticus",
        "description": "A small, social bird commonly found near human settlements.",
        "habitat": "Gardens, cities and agricultural areas",
        "diet": "Seeds, grains and insects",
        "lifespan": "3–5 years",
        "facts": [
            "Sparrows are highly social birds.",
            "They commonly build nests near buildings.",
            "They communicate through chirping."
        ]
    },

    "kingfisher": {
        "scientific_name": "Alcedo atthis",
        "description": "A brightly coloured bird known for diving into water to catch fish.",
        "habitat": "Rivers, lakes and wetlands",
        "diet": "Fish, aquatic insects and small crustaceans",
        "lifespan": "Around 6 years",
        "facts": [
            "Kingfishers have long pointed beaks.",
            "They are excellent fish hunters.",
            "They can dive rapidly into water."
        ]
    },

    "owl": {
        "scientific_name": "Strigiformes",
        "description": "A nocturnal bird known for its large eyes and ability to hunt in low light.",
        "habitat": "Forests, grasslands and urban areas",
        "diet": "Rodents, insects and small animals",
        "lifespan": "5–20 years, depending on species",
        "facts": [
            "Most owls are active at night.",
            "They can rotate their heads significantly.",
            "Their feathers help them fly quietly."
        ]
    },

    "flamingo": {
        "scientific_name": "Phoenicopterus",
        "description": "A tall wading bird recognised by its pink feathers and long legs.",
        "habitat": "Lagoons, salt lakes and wetlands",
        "diet": "Algae, small crustaceans and plankton",
        "lifespan": "20–30 years",
        "facts": [
            "Their pink colour comes from their diet.",
            "They often stand on one leg.",
            "They live in large groups."
        ]
    },

    "woodpecker": {
        "scientific_name": "Picidae",
        "description": "A bird known for tapping and drilling into tree trunks.",
        "habitat": "Woodlands and forests",
        "diet": "Insects, larvae, seeds and fruits",
        "lifespan": "4–12 years, depending on species",
        "facts": [
            "They use their beaks to find insects.",
            "Their feet help them cling to tree trunks.",
            "They have adaptations that protect their brains."
        ]
    }
}


def get_bird_info(bird_name):
    bird_name = bird_name.lower()

    aliases = {
        "indian peafowl": "peacock",
        "indian peacock": "peacock",
        "rose-ringed parakeet": "parrot",
        "ring-necked parakeet": "parrot"
    }

    for alias, key in aliases.items():
        if alias in bird_name:
            return bird_database[key]

    for key, info in bird_database.items():
        if key in bird_name:
            return info

    return None