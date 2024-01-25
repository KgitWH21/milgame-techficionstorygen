import random

# Assuming story_elements is your organized data dictionary
# ...

story_elements = {
    "STORY_DESCRIPTOR": [
        "allegorical", "dark", "dramatic", "epic", "humorous", "light-hearted", "metaphorical", "noir", 
        "parody", "psychological", "romantic", "satirical", "serious", "surreal", "tragic", "wacky", "weird"
    ],
    "CHARACTER_DESCRIPTOR": [
        "acrobatic", "awkward", "alienated", "altruistic", "ambitious", "antisocial", "arrogant", "atheistic", 
        "artistic", "athletic", "attractive", "biased", "bigoted", "boastful", "boring", "brave", "brutal", 
        "burnt-out", "calm", "charismatic", "clumsy", "committed", "compassionate", "complacent", "composed", 
        "conceited", "conformist", "confused", "contemplative", "corrupt", "courageous", "cowardly", "crazy", 
        "creative", "crippled", "cruel", "cunning", "cynical", "delusional", "depressed", "detached", "disillusioned", 
        "distant", "divorced", "domineering", "doomed", "driven", "drunken", "educated", "enduring", "energetic", 
        "ethical", "experienced", "famous", "fearful", "fear-ridden", "focused", "forceful", "friendly", "frustrated", 
        "funny", "generous", "gentle", "graceful", "greedy", "grim", "happy", "hateful", "heroic", "humble", 
        "hypocritical", "hysterical", "ignorant", "ignored", "illogical", "indecisive", "industrious", "inhibited", 
        "infamous", "innocent", "insane", "intelligent", "intimidating", "intuitive", "irrational", "kind", "laid-back", 
        "lazy", "logical", "lonely", "lucky", "manipulative", "materialistic", "mean-spirited", "melancholy", "militant", 
        "miserable", "miserly", "misguided", "misunderstood", "mysterious", "mystic", "naive", "narrow-minded", "negative", 
        "neurotic", "newlywed", "nostalgic", "nurturing", "obedient", "obscure", "obsessive", "old", "open-minded", 
        "opinionated", "opportunistic", "optimistic", "outgoing", "overworked", "patriotic", "patronizing", "peaceful", 
        "peace-loving", "persistent", "persuasive", "pessimistic", "philosophical", "pious", "plain", "poised", "poor", 
        "pragmatic", "predictable", "principled", "plucky", "rebellious", "religious", "romantic", "ruthless", "sadistic", 
        "scatterbrained", "seasoned", "secretive", "serene", "serious", "short-tempered", "sickly", "silly", "social", 
        "spendthrift", "spiritual", "stingy", "stressed", "strong", "studious", "stupid", "suave", "tired", "ugly", 
        "unambitious", "unathletic", "unbalanced", "uncreative", "unethical", "unfriendly", "unhappy", "unpredictable", 
        "unremarkable", "unstable", "unwise", "vicious", "violent", "weak", "wealthy", "well-traveled", "wise", "withdrawn", "youthful"
    ],
    "STORY_TYPE": [
        "action", "adventure", "caper", "character study", "comedy", "conflict", "conspiracy", "crime", "drama", 
        "horror", "mystery", "quest", "relationship", "revenge", "romance", "slice-of-life", "thriller", "tragedy", "transformation"
    ],
    # ... other categories like BASIC_EVENT, MILITARY_SCENARIO, etc.
}

story_elements["BASIC_EVENT"] = [
    "accident", "addiction", "adoration", "advice", "alienation", "argument", "apocalyptic event", "betrayal", 
    "birth", "compromise", "confession", "conversion", "critical injury", "death", "deception", "delusion", 
    "destruction", "discovery", "dream", "education", "engagement", "failure", "flashback", "funeral", 
    "getting lost", "growth", "guilt", "hunting", "inheritance", "intimidation", "infiltration", "insight", 
    "joke", "journey", "keepsake", "lecture", "longing", "miscommunication", "misunderstanding", "natural disaster", 
    "party", "political conflict", "premonition", "promotion", "reconciliation", "repentance", "research", 
    "resignation", "revelation", "service", "smuggling", "spiritual experience", "sport", "spying", "surgery", 
    "surrender", "temptation", "theft", "training", "tragedy", "travel", "treason", "quest", "unveiling", 
    "violence", "war", "wedding"
]


# Example for other categories, following the same structure:
story_elements["MILITARY_SCENARIO"] = [
    "Pre-Wartime", "Wartime", "Post-Wartime", "Peace time"
]

story_elements["MILITARY_PROTAGONIST"] = [
    "Junior Enlisted member", "Mid-Career Enlisted member", "Senior Enlisted member",
    "Junior Officer", "Mid-Career Officer", "Senior Officer", "Veteran", "Civilian affiliated with the military",
    "Contractor affiliated with the military", "Dependent spouse", "Dependent child"
]

story_elements["TECHNOLOGY_OBJECT"] = [
    "T-shirt", "Jeans", "Hoodie", "Dress", "Suit", "Blazer", "Skirt", "Shorts", "Tank top", "Sweater", "Cardigan",
    "Leggings", "Joggers", "Cargo pants", "Leather jacket", "Trench coat", "Parka", "Bomber jacket", "Raincoat",
    "Beanie", "Baseball cap", "Fedora", "Sun hat", "Beret", "Scarf", "Gloves", "Mittens", "Sunglasses", 
    "Prescription glasses", "Watch", "Bracelet", "Necklace", "Earrings", "Ring", "Belt", "Tie", "Bow tie", 
    "Pocket square", "Socks", "Stockings", "Tights", "Boots", "Sneakers", "High heels", "Sandals", "Loafers", 
    "Slippers", "Backpack", "Handbag", "Clutch bag", 
    # Weapons
    "Sword", "Longbow", "Crossbow", "Spear", "Shield", "Axe", "Mace", "Dagger", "Halberd", "War hammer", "Flail", 
    "Blowgun", "Slingshot", "Bo staff", "Nunchaku", "Katana", "Rapier", "Scimitar", "Gladius", "Pike", "Trident", 
    "Club", "Javelin", "Morning star", "Kukri", "Sabre", "Bowie knife", "Bayonet", "Machete", "Compound bow", 
    "Taser", "Revolver", "Semi-automatic pistol", "Rifle", "Shotgun", "Sniper rifle", "Submachine gun", "Machine gun", 
    "Grenade", "Rocket launcher", "Flamethrower", "Landmine", "Naval mine", "Torpedo", "Guided missile", "Tactical knife", 
    "Stun baton", "Pepper spray", "Electrified baton", "Bola",
    # Items
    "Toothbrush", "Toothpaste", "Soap", "Shampoo", "Conditioner", "Towel", "Comb", "Hair dryer", "Mirror", 
    "Deodorant", "Nail clippers", "Razor", "Toilet paper", "Facial tissue", "Moisturizer", "Sunscreen", "Lip balm", 
    "Hand sanitizer", "Laundry detergent", "Dish soap", "Sponge", "Trash bags", "Paper towels", "Light bulbs", 
    "Batteries", "Scissors", "Tape", "Notebook", "Pen", "Pencil", "Eraser", "Stapler", "Paper clips", "Rubber bands", 
    "USB drive", "Charger for phone", "Headphones", "Alarm clock", "Keys", "Wallet", "Sunglasses", "Umbrella", 
    "Water bottle", "Coffee mug", "Tea kettle", "Microwave", "Oven mitts", "Refrigerator magnets", "Can opener", "Corkscrew"
]

story_elements["TECHNOLOGY_FUNCTION"] = [
    "A Fall from Grace", "A Quest for Knowledge", "Addiction", "Alienation", "Beauty", "Beginnings", "Betrayal", "Borders", 
    "Coming of Age", "Conservation", "Control", "Corruption", "Courage", "Crossroads", "Danger", "Death", "Deception", 
    "Depression", "Disorder", "Doomsday", "Endings", "Enslavement", "Evil", "Failure", "Family", "Fate", "Freedom", 
    "Friendship", "Greed", "Health", "Honor", "Hope", "Identity", "Illness", "Immortality", "Inflexibility", "Injustice", 
    "Innocence", "Instability", "Isolation", "Journeys", "Justice", "Knowledge", "Loss", "Love", "Materialism", "Mystery", 
    "Nature", "Obstacles", "Order", "Passage of Time", "Peace", "Perseverance", "Poverty", "Power", "Pride", "Progress", 
    "Purity", "Purpose", "Rebellion", "Rebirth", "Recognition", "Redemption", "Refuge", "Religion", "Revenge", 
    "Rite of Passage", "Sacrifice", "Stagnation", "Success", "Suffering", "Superstitions: Bad Luck", "Superstitions: Good Luck", 
    "Survival", "Teamwork", "Technology", "Tradition", "Transformation", "Trust", "Truth", "Unity", "Vanity", "Vice", 
    "Violence", "Virtue", "Vulnerability", "War", "Wealth"
]

story_elements["EMOTION"] = [
    "Acceptance", "Admiration", "Adoration", "Agitation", "Amazement", "Amusement", "Anger", "Anguish", "Annoyance", 
    "Anticipation", "Anxiety", "Appalled", "Apprehension", "Awe", "Betrayed", "Bitterness", "Certainty", "Concern", 
    "Confidence", "Conflicted", "Confusion", "Connectedness", "Contempt", "Curiosity", "Defeat", "Defensiveness", 
    "Defiance", "Denial", "Depressed", "Desire", "Despair", "Desperation", "Determination", "Devastation", "Disappointment", 
    "Disbelief", "Discouragement", "Disgust", "Disillusionment", "Dissatisfaction", "Doubt", "Dread", "Eagerness", 
    "Elation", "Emasculation", "Embarrassment", "Empathy", "Envy", "Euphoria", "Excitement", "Fear", "Fearlessness", 
    "Flustered", "Frustration", "Giddiness", "Gratitude", "Grief", "Guilt", "Happiness", "Hatred", "Homesickness", 
    "Hopefulness", "Horror", "Humbled", "Humiliation", "Hurt", "Hysteria", "Impatience", "Inadequacy", "Indifference", 
    "Indignation", "Insecurity", "Inspired", "Intimidation", "Irritation", "Jealousy", "Joy", "Loneliness", "Longing", 
    "Love", "Lust", "Misery", "Moodiness", "Moved", "Neglected", "Nervousness", "Nostalgia", "Obsession", "Overwhelmed", 
    "Panic", "Paranoia", "Peacefulness", "Pity", "Pleased", "Powerlessness", "Pride", "Rage", "Regret", "Relief", 
    "Reluctance", "Remorse", "Resentment", "Resignation", "Revulsion", "Sadness", "Sappiness", "Satisfaction", 
    "Schadenfreude", "Scorn", "Self-loathing", "Self-pity", "Shame", "Shock", "Skepticism", "Smugness", "Somberness", 
    "Stunned", "Surprise", "Suspicion", "Sympathy", "Terror", "Tormented", "Unappreciated", "Uncertainty", "Unease", 
    "Validation", "Valued", "Vengefulness", "Vindication", "Vulnerability", "Wanderlust", "Wariness", "Wistfulness", 
    "Worry", "Worthlessness"
]

story_elements["EMOTION_AMPLIFIER"] = [
    "Addiction", "Arousal", "Attraction", "Boredom", "Cold", "Dehydration", "Distraction", "Exhaustion", 
    "Hangover", "Heat", "Hunger", "Illness", "Inebriation", "Lethargy", "Overstimulation", "Pain", 
    "Relaxation", "Stress"
]

story_elements["SUPERHUMAN_ABILITY"] = [
    "Super strength", "Flight", "Telekinesis", "Telepathy", "Invisibility", "Shape-shifting", "Time travel", 
    "Super speed", "Healing factor", "Invulnerability", "X-ray vision", "Mind control", "Energy manipulation", 
    "Weather control", "Pyrokinesis", "Cryokinesis", "Electrokinesis", "Teleportation", "Animal communication", 
    "Plant manipulation", "Sonic scream", "Gravity manipulation", "Size-shifting", "Precognition", "Intangibility", 
    "Force field generation", "Enhanced agility", "Enhanced senses", "Astral projection", "Illusion creation", 
    "Elemental control", "Molecular manipulation", "Enhanced intelligence", "Longevity", "Memory manipulation", 
    "Regeneration", "Underwater breathing", "Night vision", "Enhanced reflexes", "Superhuman endurance", 
    "Magnetism control", "Light manipulation", "Darkness manipulation", "Sound manipulation", "Elasticity", 
    "Acid generation", "Life force absorption", "Probability manipulation", "Cosmic energy manipulation", 
    "Multi-dimensional awareness", "Clairvoyance", "Psychometry", "Biokinesis", "Portal creation", 
    "Time manipulation", "Duplication", "Enhanced crafting", "Hypnosis", "Aura reading", "Empathy", 
    "Sonic flight", "Phasing", "Radiation control", "Necromancy", "Gravity defiance", "Spirit communication", 
    "Reality warping", "Omnilingualism", "Dream manipulation", "Shapeshifting into animals", "Invisibility to technology", 
    "Technopathy", "Energy absorption", "Seismic manipulation", "Ferrokinesis", "Photographic reflexes", 
    "Animal morphing", "Antigravity", "Spatial awareness", "Quantum manipulation", "Omni-presence", 
    "Weather resistance", "Fire breathing", "Sublimation", "Superhuman tracking", "Energy constructs", 
    "Shadow melding", "Echolocation", "Kinetic energy manipulation", "Camouflage", "Water manipulation", 
    "Sand manipulation", "Cybernetic enhancement", "Illusion resistance", "Age manipulation", "Air manipulation", 
    "Density control", "Sonic manipulation", "Cosmic awareness", "Chronolinguistics", "Bio-luminescence manipulation", 
    "Tychokinesis", "Sonic mimicry", "Electromagnetic spectrum vision", "Pheromone control", "Gravitational wave sensing", 
    "Molecular gastronomy", "Retrocognition", "Emotional resonance", "Quantum tunneling", "Memory palace", 
    "Auric manipulation", "Chrono-ventriloquism", "Metaphysical synesthesia", "Lucid dream control", 
    "Atmospheric adaptation", "Psychometric telepathy", "Cryptid communication", "Panmnesia", "Echo-location in vacuum", 
    "Bioluminescent communication", "Subatomic manipulation", "Reality anchoring", "Geomantic divination", 
    "Entropic reversal", "Harmonic resonance", "Intuitive polyglotism", "Emotional echo-location", "Temporal inertia", 
    "Microscopic vision", "Cryptographic intuition", "Sympathetic healing", "Psychosomatic manipulation", 
    "Eidetic echolocation", "Gravitational empathy", "Infrasound communication", "Chrono-empathy", "Linguistic absorption", 
    "Nutritional transmutation", "Tactile psychokinesis", "Spectral music", "Elemental empathy", "Precognitive crafting", 
    "Selective intangibility", "Retroactive immunity", "Aural psychometry", "Gravitokinetic combat", 
    "Ideokinetic projection", "Temporal echo", "Quantum entanglement communication", "Dimensional digestion", 
    "Cosmic frequency tuning", "Planetary empathy", "Stellar navigation", "Black hole mimicry", "Galactic echo location", 
    "Supernova ignition", "Nebula breath", "Vacuum adaptation", "Astro-morphing", "Quantum uncertainty manipulation", 
    "Event horizon traversal", "Cosmic web awareness", "Dark matter manipulation", "Wormhole weaving", 
    "Solar flare emission", "Molecular orbit alteration", "Gravitational singularity", "Interstellar seed dispersal", 
    "Dark energy absorption", "Pulsar pulse generation", "Exoplanetary resonance", "Cosmic dust shaping", 
    "Void speech", "Starlight absorption", "Galaxy whispering", "Interdimensional aperture", "Alien ecosystem integration", 
    "Stellar core walking", "Quantum leap", "Cosmic storm riding", "Orbital manipulation", "Galactic chorus", 
    "Quasar vision", "Astro-linguistics", "Exotic matter mastery", "Comet tail surfing", "Interstellar breath", 
    "Cosmic regeneration", "Nebular weaving", "Planetary assimilation", "Star seed germination", "Void creation", 
    "Cosmic symbiosis", "Chronal stasis", "Universal language translation", "Graviton surfing", "Exotic particle generation", 
    "Cosmic harmony"
]

story_elements["VIDEO_GAME_FRANCHISE"] = [
    "The Legend of Zelda", "Final Fantasy", "Mass Effect", "The Elder Scrolls", "Dragon Age", "The Witcher", 
    "Metal Gear Solid", "Uncharted", "Assassin's Creed", "Red Dead Redemption", "Tomb Raider", "Bioshock", 
    "Fallout", "Halo", "God of War", "The Last of Us", "Resident Evil", "Silent Hill", "Kingdom Hearts", 
    "Gears of War", "Portal", "Life is Strange", "Half-Life", "Deus Ex", "Dishonored", "Batman: Arkham series", 
    "Horizon Zero Dawn", "Far Cry", "Borderlands", "Grand Theft Auto", "Call of Duty (Campaigns)", "Dark Souls", 
    "Bloodborne", "Persona", "Elder Scrolls", "Witcher", "Cyberpunk 2077", "Detroit: Become Human", "Heavy Rain", 
    "Beyond: Two Souls", "Telltale's The Walking Dead", "Mass Effect", "Dragon Quest", "Infamous", 
    "Shadow of the Colossus", "L.A. Noire", "Alan Wake", "Kingdom Come: Deliverance", "The Wolf Among Us", 
    "Fire Emblem", "Yakuza", "NieR", "Devil May Cry", "Phoenix Wright: Ace Attorney", "Max Payne", 
    "Xenoblade Chronicles", "Star Wars: Knights of the Old Republic", "Journey", "The Banner Saga", 
    "The Stanley Parable", "Undertale", "Spec Ops: The Line", "Danganronpa", "Dead Space", "Ori and the Blind Forest", 
    "Metro series", "The Outer Worlds", "Tales series", "Fable", "Chrono Trigger", "Shenmue", "EarthBound", 
    "The Longest Journey", "Planescape: Torment", "Baldur's Gate", "Myst", "Catherine", "StarCraft", 
    "LittleBigPlanet", "Octopath Traveler", "Valkyria Chronicles", "Disco Elysium", "Syberia", "Professor Layton", 
    "Banjo-Kazooie", "Legend of Dragoon", "Brothers: A Tale of Two Sons", "Braid", "Amnesia: The Dark Descent", 
    "SOMA", "The Witness", "Until Dawn", "Kentucky Route Zero", "Limbo", "Inside", "Oxenfree", "Pillars of Eternity", 
    "Ghost of Tsushima", "Control", "Hellblade: Senua's Sacrifice"
]

story_elements["CHARACTER_GENDER"] = [
        "male", "female", "ungendered", "transgender"    
    ]

# Now, all your categories are formatted and ready for use in your story generator.





def select_random_element(category):
    return random.choice(story_elements[category])

def generate_story():
    story = f"This story is about a {select_random_element('CHARACTER_DESCRIPTOR')} {select_random_element('CHARACTER_GENDER')} {select_random_element('MILITARY_PROTAGONIST')} during {select_random_element('MILITARY_SCENARIO')}. "
    story += f"The major event of the story involves {select_random_element('BASIC_EVENT')}. "
    story += f"The story starts with {select_random_element('STORY_DESCRIPTOR')} theme, "
    story += f"and ends with {select_random_element('STORY_TYPE')}. "
    story += f"The central technology object is the {select_random_element('TECHNOLOGY_FUNCTION')} {select_random_element('TECHNOLOGY_OBJECT')}. "
    story += f"This causes {select_random_element('EMOTION_AMPLIFIER')} leading to {select_random_element('EMOTION')}. "
    story += f"The protagonist has a superhuman ability: {select_random_element('SUPERHUMAN_ABILITY')}. "
    story += f"Elements and themes from the video game {select_random_element('VIDEO_GAME_FRANCHISE')} are adapted in this story."

    return story

# Generate a story
print(generate_story())
