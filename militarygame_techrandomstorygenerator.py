import random

# Assuming story_elements is your organized data dictionary
# ...

story_elements = {
    "STORY_DESCRIPTOR": [
        "allegorical", "dark", "dramatic", "epic", "humorous", "light-hearted", "metaphorical", "noir", "parody", "psychological", "romantic", "satirical", "serious", 
        "surreal", "tragic", "wacky", "weird", "absurdist", "action-packed", "adventurous", "bittersweet", "captivating", "chilling", "complex", "contemplative", "cynical", 
        "deep", "emotional", "enigmatic", "exhilarating", "fantastical", "gripping", "heartwarming", "introspective", "ironic", "melancholic", "mysterious", "nostalgic", 
        "poignant", "provocative", "quirky", "reflective", "romanticized", "scary", "suspenseful", "thought-provoking", "thrilling", "uplifting", "whimsical", "wistful", "zany", 
        "angst-ridden", "atmospheric", "brooding", "celebratory", "claustrophobic", "comedic", "compelling", "confrontational", "cryptic", "dreamlike", "eerie", "energetic", 
        "evocative", "exotic", "explosive", "fanciful", "foreboding", "heartbreaking", "idyllic", "imaginative", "impressionistic", "insightful", "intense", "lighthearted", 
        "magical", "menacing", "mesmerizing", "morbid", "mystical", "optimistic", "otherworldly", "outlandish", "over-the-top", "pastoral", "pensive", "philosophical", 
        "playful", "poetic", "powerful", "provoking", "puzzling", "raw", "realistic", "relatable", "resonant", "retro", "revealing", "revolutionary", "rhythmic", "rich", 
        "sardonic", "sentimental", "shocking", "simplistic", "sinister", "spellbinding", "spine-tingling", "spiritual", "spooky", "stark", "stimulating", "strange", "striking", 
        "surrealistic", "tense", "touching", "tranquil", "twisted", "unconventional", "vibrant", "visceral", "visual", "vivid", "wholesome", "witty", "wondrous"
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
        "unremarkable", "unstable", "unwise", "vicious", "violent", "weak", "wealthy", "well-traveled", "wise", "withdrawn", "youthful", "foolish", "vindictive",
        "vengeful", "horrible"
    ],
    "STORY_TYPE": [
        "action", "adventure", "caper", "character study", "comedy", "conflict", "conspiracy", "crime", "drama", "horror", "mystery", "quest", "relationship", "revenge", 
        "romance", "slice-of-life", "thriller", "tragedy", "transformation", "fantasy", "science fiction", "historical", "political", "satire", "dystopian", "utopian", 
        "supernatural", "paranormal", "coming-of-age", "espionage", "war", "post-apocalyptic", "magical realism", "mythology", "fairy tale", "superhero", "cyberpunk", 
        "steampunk", "western", "noir", "heist", "psychological", "spiritual", "gothic", "survival", "eco-fiction", "time travel", "space opera", "biographical", 
        "alternative history", "urban fantasy", "erotic", "legal", "medical", "sports", "educational/instructional", "animal/nature", "techno-thriller", "family saga", "allegory"
        "adventure romance", "alien encounter", "art heist", "artificial intelligence uprising", "body swap", "buddy cop", "celebrity biography", "climate fiction", 
        "clone conspiracy", "corporate espionage", "cross-cultural", "cyber rebellion", "deep sea exploration", "desert survival", "detective noir", "dream world exploration", 
        "dystopian rebellion", "elderly protagonist's journey", "epic poetry", "experimental", "fable", "folklore inspired", "future dystopia", "galactic exploration", 
        "genetic engineering ethics", "ghost story", "global disaster", "high seas adventure", "historical romance", "intergalactic war", "interplanetary exploration", 
        "journey to the center of the earth", "lost civilization", "love triangle", "martial arts epic", "medical drama", "medieval fantasy", "mind control thriller", 
        "multigenerational saga", "mythic retelling", "pirate adventure", "post-war drama", "prehistoric fiction", "psychological horror", "robotic uprising", "shakespearean", 
        "space colonization", "spy thriller", "time loop", "virtual reality adventure"
    ],

    "NARRATIVE_PERSPECTIVE": [
        "First Person Singular ('I')",
        "First Person Plural ('We')",
        "First Person Peripheral",
        "First Person Unreliable",
        "First Person Stream of Consciousness",
        "Epistolary First Person",
        "Second Person ('You')",
        "Second Person Interactive",
        "Third Person Limited",
        "Third Person Multiple",
        "Third Person Omniscient",
        "Third Person Objective",
        "Third Person Stream of Consciousness",
        "Third Person Epistolary",
        "Third Person Cinematic",
        "Third Person Unreliable Narrator"
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
    "violence", "war", "wedding", "betrayal", "deception", "poverty", "addiction", "corruption", "prejudice", "jealousy", "disease", "isolation", "failure", "guilt", "grief", 
    "obsession", "fear", "rejection", "rage", "desperation", "manipulation", "exile", "injustice", "temptation", "oppression", "war", "famine", "disaster", "drought", "storm", 
    "wildfire", "earthquake", "accident", "competition", "hostility", "betrayal", "blackmail", "conspiracy", "distrust", "envy", "paranoia", "rebellion", "repression", "scandal", 
    "terrorism", "torture", "trauma", "upheaval", "vendetta", "vice", "violence", "xenophobia", "zealotry",     "Acceptance", "Admiration", "Adoration", "Agitation", "Amazement", "Amusement", "Anger", "Anguish", "Annoyance", 
    "Anticipation", "Anxiety", "Appalled", "Apprehension", "Awe", "Betrayed", "Bitterness", "Certainty", "Concern", 
    "Confidence", "Conflicted", "Confusion", "Connectedness", "Contempt", "Curiosity", "Defeat", "Defensiveness", 
    "Defiance", "Denial", "Depressed", "Desire", "Despair", "Desperation", "Determination", "Devastation", "Disappointment", 
    "Disbelief", "Discouragement", "Disgust", "Disillusionment", "Dissatisfaction", "Doubt", "Dread", "Eagerness", 
    "Elation", "Emasculation", "Embarrassment", "Empathy", "Envy", "Euphoria", "Excitement", "Fear", "Fearlessness", 
    "Flustered", "Frustration", "Giddiness", "Gratitude", "Grief", "Guilt", "Happiness", "Hatred", "Homesickness", 
    "Hopefulness", "Horror", "Humility", "Humiliation", "Hurt", "Hysteria", "Impatience", "Inadequacy", "Indifference", 
    "Indignation", "Insecurity", "Inspired", "Intimidation", "Irritation", "Jealousy", "Joy", "Loneliness", "Longing", 
    "Love", "Lust", "Misery", "Moodiness", "Moved", "Neglected", "Nervousness", "Nostalgia", "Obsession", "Overwhelmed", 
    "Panic", "Paranoia", "Peacefulness", "Pity", "Pleased", "Powerlessness", "Pride", "Rage", "Regret", "Relief", 
    "Reluctance", "Remorse", "Resentment", "Resignation", "Revulsion", "Sadness", "Sappiness", "Satisfaction", 
    "Schadenfreude", "Scorn", "Self-loathing", "Self-pity", "Shame", "Shock", "Skepticism", "Smugness", "Somberness", 
    "Stunned", "Surprise", "Suspicion", "Sympathy", "Terror", "Tormented", "Unappreciated", "Uncertainty", "Unease", 
    "Validation", "Valued", "Vengefulness", "Vindication", "Vulnerability", "Wanderlust", "Wariness", "Wistfulness", 
    "Worry", "Worthlessness","Fall from Grace", "Quest for Knowledge", "Addiction", "Alienation", "Beauty", "Beginnings", "Betrayal", "Borders", 
    "Coming of Age", "Conservation", "Control", "Corruption", "Courage", "Crossroads", "Danger", "Death", "Deception", 
    "Depression", "Disorder", "Doomsday", "Endings", "Enslavement", "Evil", "Failure", "Family", "Fate", "Freedom", 
    "Friendship", "Greed", "Health", "Honor", "Hope", "Identity", "Illness", "Immortality", "Inflexibility", "Injustice", 
    "Innocence", "Instability", "Isolation", "Journeys", "Justice", "Knowledge", "Loss", "Love", "Materialism", "Mystery", 
    "Nature", "Obstacles", "Order", "Passage of Time", "Peace", "Perseverance", "Poverty", "Power", "Pride", "Progress", 
    "Purity", "Purpose", "Rebellion", "Rebirth", "Recognition", "Redemption", "Refuge", "Religion", "Revenge", 
    "Rite of Passage", "Sacrifice", "Stagnation", "Success", "Suffering", "Superstitions: Bad Luck", "Superstitions: Good Luck", 
    "Survival", "Teamwork", "Technology", "Tradition", "Transformation", "Trust", "Truth", "Unity", "Vanity", "Vice", 
    "Violence", "Virtue", "Vulnerability", "War", "Wealth", "fire", "typhoon", "jail time", "traffic jam", "street fight", "darkness",
    "power outage", "blizzard", "tornado", "famine", "dehydration", "pestilience", "pandemic", "inflation", "election", "nemesis", "rival", "adversary", "hater", "act of God",
    "digital troll", "boss", "mini-boss", "race", "competition", "ex-boyfriend", "ex-girlfriend", "ex-lover", "ex-boss", "parents", "mother-in-law", "father-in-law", "brother"
    "sister", "opponent", "drug dealer", "crooked cop", "gang member", "thug", "overlord", "demonlord", "restless ghost" 
]


# Example for other categories, following the same structure:
story_elements["MILITARY_SCENARIO"] = [
    "Pre-Wartime", "Wartime", "Post-Wartime", "Peace time"
]

story_elements["TIME_PERIOD"] = [
    "Near-present (10 - 30 Earth years from now)", "Future-present (30 - 100 Earth years from now)", "Future-past (100 - 2000 years from now)", "Distant future (2000 - 10000 Earth years from now)",
    "Future Frontier (10000 - 1M Earth years from now)", "Present Future (10000 - 1M Earth years from now)", "Forever Future (1M - 13B Earth years from now)"
]

story_elements["Culture_Inspiration"] = [
    "Chinese", "Singaporean", "Taiwanese", "Modern Japanese", "Okinawan", "Hokkaido Japanese", "American - California", "American - Texas", "American - Hawaiian", "American - Alaskan",
    "American - Las Vegas", "American - Washington DC", "American - Deep South", "Mexican", "Maldivian", "Italian", "Mongolian", "Japanese - Yonaguni", "Japanese - Edo", "Japanese - Meiji",
    "Imperial Japanese"
]

story_elements["World_State"] = ["Rising", "Expanding",  "Shifting", "Dying", "Fading",  "Corrupted", "Sustaining", "Stagnant",  "Forgotten", "Dreaming", "Fractured", "Unwritten",  "Contested",
    "Mirrored", "Observed", "Paradoxical" 
]

story_elements["world_scopes"] = [
    "microscopic-sized", 
    "subatomic-sized",
    "interior-sized", 
    "neighborhood-sized", 
    "city-sized", 
    "region/province-sized", 
    "nation-sized", 
    "continent-sized", 
    "planet-sized", 
    "solar system-sized", 
    "galaxy-sized", 
    "universe-sized" 
]

story_elements["MILITARY_PROTAGONIST"] = [
    "Junior Enlisted", "Mid-Career Enlisted", "Senior Enlisted",
    "Junior Officer", "Mid-Career Officer", "Senior Officer", "Veteran", "military affiliated civilian",
    "military affiliated contractor", "Dependent spouse", "Dependent child", "grizzled combat veteran", "retiree", "civilian who never served",
    "Conscript", "Child soldier", "With unknown military Status", "Defector", "Consciencious Objector", "Mercenary", "Lone Wolf", 
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
    "Relaxation", "Stress", "Drunken stupor", "Drunken rage", "Bloodlust", "Terrified", "Rage", "Hypoxic", "Poisoned",
    "Drowning panic", "Suicidal thoughts", "Acid trip", "Dreamy hallucination", "Nightmare hallucination", "Uncontrolled laughter",
    "Endless crying", "Dark depression", "Neuroticism", "Animalistic rage", "Suffocating Isolation", "Intense loneliness", "Hedonistic binge",
    "Stress eating", "Starvation", "Blood slowing", "Blood rushing", "Amnesia", "Blindness", "Deafness", "Body constriction", "Vomit inducing vertigo"
    "General anxiety"
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
    "Ghost of Tsushima", "Control", "Hellblade: Senua's Sacrifice" , "Final Fantasy IV", "Final Fantasy V", "Final Fantasy VI",
    "Final Fantasy VII", "Final Fantasy VIII", "Final Fantasy IX", "Final Fantasy X", "Final Fantasy XII", "Final Fantasy XIII",
    "Final Fantasy XIII-2", "Lightning Returns: Final Fantasy XIII", "Final Fantasy Tactics", "Xenoblade Chronicles 2", "Xenoblade Chronicles 3",  "Xenoblade Chronicles X", "The Legend of Zelda: A Link to the Past"
]

story_elements["CHARACTER_GENDER"] = [
        "male","male","male","male","female", "female", "female", "female", "ungendered", "transgender"    
    ]

story_elements["JOBS"] = [
    "KC-135 Stratotanker Pilot", "F-16 Fighting Falcon Pilot", "B-2 Spirit Bombardier", "C-17 Globemaster III Navigator", "Weapons Systems Officer", "Drone Pilot",
    "Intelligence Analyst", "Aerospace Propulsion Specialist", "Cyber Transport Systems Specialist", "Equal Opportunity Specialist", "Special Investigations Officer",
    "Fire Protection Specialist", "Aerospace Ground Equipment Specialist", "Aircraft Loadmaster", "Aircraft Electrical and Environmental Systems Specialist",
    "Aircraft Metals Technology Specialist", "Airfield Management Officer", "Air Traffic Control Officer", "Civil Engineer Officer", "Medical Service Corps Officer",
    "Public Affairs Officer", "Judge Advocate General", "Flight Surgeon", "Mental Health Nurse", "Dental Hygienist", "Surgical Services Specialist", "Pharmacy Technician",
    "Pararescue Specialist", "Combat Weather Officer", "Emergency Management Officer", "Cyberspace Operations Officer", "Space Systems Operations Specialist",
    "Nuclear and Missile Operations Officer", "Security Forces Officer", "Contracting Officer", "Logistics Readiness Officer", "Aircraft Maintenance Officer",
    "Diet Therapy Specialist", "Operations Intelligence Specialist", "Health Services Management Specialist", "Personnel Officer", "Financial Management Officer",
    "Bioenvironmental Engineer Officer", "Communications and Information Officer", "Aerospace Medicine Specialist", "Historian", "Weather Officer", "Chaplain", "Psychologist",
    "Special Agent"

    #Army Jobs
        "AH-64 Apache Helicopter Pilot", "Military Intelligence Officer", "Cyber Operations Specialist", "Combat Medic Specialist", "Signal Corps Officer", "Civil Affairs Officer",
    "Psychological Operations Specialist", "Logistics Support Specialist", "Ranger Qualified Infantryman", "Special Forces Engineer Sergeant", "Military Police Officer",
    "Fire Support Specialist", "Counterintelligence Agent", "Explosive Ordnance Disposal Specialist", "Air Defense Artillery Officer", "Public Affairs Specialist", "Transportation Management Coordinator",
    "Finance Management Technician", "Chemical, Biological, Radiological, and Nuclear (CBRN) Officer", "Human Resources Specialist", "JAG - Judge Advocate General's Corps Attorney",
    "Aviation Operations Specialist", "Unmanned Aerial Vehicle Operator", "Dental Specialist", "Healthcare Administration Officer", "Wheeled Vehicle Mechanic", "Chaplain", "Information Technology Specialist",
    "Paralegal Specialist", "Army Bandperson", "Environmental Science/Engineering Officer", "Medical Service Corps Officer", "Pharmacy Specialist", "Aircraft Powerplant Repairer",
    "Quartermaster Officer", "Field Artillery Firefinder Radar Operator", "Special Forces Medical Sergeant", "Armor Officer", "Nuclear Medical Science Officer", "Aircraft Electrician",
    "Carpentry and Masonry Specialist", "Biomedical Equipment Specialist", "Criminal Investigations Special Agent", "Horizontal Construction Engineer", "Multimedia Illustrator", "Petroleum Supply Specialist",
    "Signal Support Systems Specialist", "Watercraft Operator", "Geospatial Engineer", "Army National Guard Sniper"
    #Navy Jobs
    "Naval Aviator - F/A-18 Hornet Pilot", "Cryptologic Warfare Officer", "Explosive Ordnance Disposal (EOD) Officer", 
    "Navy SEAL Officer", "Nuclear Submarine Officer", "Naval Flight Officer - E-2 Hawkeye", "Surface Warfare Officer - Destroyer",
    "Naval Intelligence Officer", "Navy Chaplain", "Healthcare Administration Officer", "Naval Reactors Engineer", 
    "Fire Controlman - Aegis", "Logistics Specialist", "Hospital Corpsman", "Cryptologic Technician", "Aviation Structural Mechanic",
    "Information Systems Technician", "Machinist's Mate - Nuclear", "Naval Aircrewman - MH-60 Seahawk", "Sonar Technician - Submarine",
    "Special Warfare Boat Operator", "Navy Diver", "Aviation Ordnanceman", "Electronics Technician - Submarine", "Aviation Machinist's Mate",
    "Master-at-Arms", "Operations Specialist", "Culinary Specialist", "Construction Mechanic - Seabees", "Navy Musician",
    "Aerospace Maintenance Duty Officer", "Oceanography Officer", "Public Affairs Officer", "Civil Engineer Corps Officer",
    "Naval Flight Surgeon", "Cyber Warfare Engineer", "Supply Corps Officer", "Nuclear Power School Instructor", "Environmental Health Officer",
    "Physical Therapy Officer", "Aviation Electrician's Mate", "Mass Communication Specialist", "Personnel Specialist", "Gas Turbine System Technician",
    "Religious Program Specialist", "Aviation Boatswain's Mate", "Navy Judge Advocate General's Corps Officer", "Dental Corps Officer",
    "Medical Corps Officer", "Naval Aviator - MH-53 Sea Dragon Pilot"
    #Marine Corps jobs
    "0311 - Rifleman", "0321 - Reconnaissance Marine", "0331 - Machine Gunner", "0341 - Mortarman", "0351 - Infantry Assault Marine", "0352 - Anti-tank Missileman", "0651 - Cyber Network Operator", 
    "0811 - Field Artillery Cannoneer", "0844 - Fire Control Man", "0861 - Fire Support Man", "1371 - Combat Engineer", "1391 - Bulk Fuel Specialist", "1833 - Assault Amphibious Vehicle (AAV) Crewman", 
    "2671 - Middle East Cryptologic Linguist", "4421 - Legal Services Specialist", "5821 - Criminal Investigator CID Agent", "5951 - Air Traffic Control Radar Technician", 
    "6046 - Aircraft Maintenance Administration Specialist", "6074 - Cryogenics Equipment Operator", "6174 - Helicopter Crew Chief, UH-1Y Venom", "6216 - Fixed-Wing Aircraft Crew Chief, KC-130", 
    "6256 - Fixed-Wing Aircraft Airframe Mechanic, AV-8B Harrier", "6276 - Fixed-Wing Aircraft Airframe Mechanic, F/A-18", "6286 - Fixed-Wing Aircraft Electrical Systems Technician, F-35B Lightning II", 
    "6314 - Unmanned Aerial Vehicle (UAV) Operator", "6531 - Aircraft Ordnance Technician", "6842 - Meteorology and Oceanography (METOC) Analyst Forecaster", "7011 - Expeditionary Airfield Systems Technician", 
    "7041 - Aviation Operations Specialist", "7257 - Air Traffic Controller", "7314 - Vertical TakeOff and Landing Unmanned Aerial Vehicle (UAV) Operator", "7372 - C-130 Hercules Loadmaster", 
    "7381 - C-22 Osprey Crew Chief", "8411 - Recruiters", "8421 - Career Planner", "8431 - Psychological Operations Specialist", "8652 - Reconnaissance Man, Parachute Qualified", 
    "8999 - Sergeant Major of the Marine Corps", "9051 - Religious Program Specialist", "1302 - Combat Engineer Officer", "1802 - Tank Officer", "2502 - Communications Officer", "3002 - Ground Supply Officer", 
    "3404 - Financial Management Officer", "4402 - Judge Advocate", "5803 - Military Police Officer", "6602 - Space Operations Officer", "7208 - Low Altitude Air Defense Officer", "7509 - Pilot, F/A-18 Hornet", 
    "7562 - Pilot, MV-22 Osprey"
    #US Space Force Jobs
        "Space Operations Officer", "Cyberspace Operations Officer", "Intelligence Officer", "Missile and Space Systems Maintenance Officer",
    "Space Systems Operations Specialist", "Cyber Systems Operations Specialist", "Cyber Transport Systems Specialist", "Intelligence Analyst", 
    "Sensor Operator for Remote Sensing", "Satellite Communications Operator", "Space Systems Operations Analyst", "Space Electronic Warfare Specialist", 
    "Acquisition Manager for Space Systems", "Orbital Analyst", "Aerospace Medicine Specialist", "Space Environmental Specialist", "Space Operator Assistant",
    "Spacecraft Launch and Recovery Technician", "Orbital Space Vehicle Repairman", "Extraterrestrial Habitat Architect", "Lunar Excavation Operator", 
    "Interstellar Communications Specialist", "Zero-Gravity Construction Worker", "Planetary Geologist", "Astrobiologist", "Space-Based Solar Power Engineer", 
    "Orbital Debris Removal Specialist", "Space Traffic Controller", "Deep Space Navigator", "Exoplanet Explorer", "Space Diplomacy Officer", 
    "Interplanetary Network Engineer", "Artificial Gravity Systems Technician", "Space Suit Technician", "Astro-Pharmaceutical Researcher", 
    "Cosmic Radiation Protection Specialist", "Space Tourism Coordinator", "Extraterrestrial Agriculture Specialist", "Quantum Communication Specialist", 
    "Space-Based Manufacturing Engineer", "Off-Earth Mining Technician", "Astro-Cultural Officer", "Celestial Navigation Specialist", 
    "Interstellar Trade Analyst", "Space Settlement Administrator", "Anti-Satellite (ASAT) Warfare Specialist", "Exoatmospheric Pilot"
        "Astro-Engineering Liaison", "Interorbital Threat Analyst", "Nanosatellite Swarm Coordinator", "Spaceborne AI Ethics Supervisor", 
    "Cosmic Weather Forecaster", "Spacecraft Quarantine Enforcer", "Astrocartography Expert", "Orbital Habitat Safety Inspector", 
    "Hyperspace Route Planner", "Anti-Meteoroid Defense Operator", "Lunar Logistics Specialist", "Deep Space Rescue Operative", 
    "Extra-Vehicular Activity (EVA) Combat Trainer", "Advanced Propulsion Technician", "Space Debris Analyst and Clearing Coordinator", 
    "Interstellar Signal Decryptor", "Quantum Encryption Officer", "Off-Planet Resource Rights Negotiator", "Astro-Sociologist", 
    "Exoplanetary Claim Assessor", "Interorbital Commerce Regulator", "Zero-G Medical Practitioner", "Space Fleet Supply Chain Manager", 
    "Celestial Body Mapping Specialist", "Space Sovereignty Advocate", "Extraterrestrial Ecosystems Protector", "Off-World Habitat Ethicist", 
    "Galactic Historian", "Starship Loadmaster", "Remote Sensing Data Analyst", "Space Elevator Operator", "Cosmo-Chemical Analyst", 
    "Space-Based Crisis Response Coordinator", "Interstellar Beacon Operator", "Cosmic Event Early Warning Specialist", "Wormhole Exploration Lead", 
    "Alien Technology Reverse Engineer", "Xenobiology Containment Officer", "Galactic Network Cyber Defender", "Planetary Defense Strategist", 
    "Spaceborne Humanitarian Aid Dispatcher", "Orbital Colony Legal Consultant", "Zero-G Agriculture Innovator", "SpaceTime Anomalies Investigator", 
    "Interstellar Communications Relay Architect", "Vacuum-Compatible Materials Scientist", "Space Traffic Incident Investigator", 
    "Cosmic Surveillance Systems Architect", "Offensive Space Operations Strategist", "Defensive Space Infrastructure Engineer"

]

story_elements["CHARACTER_GOALS"] = [
        "Uncover the truth about their mysterious past", "Save their hometown from an impending disaster", "Find a cure for a rare disease plaguing their family", 
        "Overthrow a tyrannical ruler and restore peace", "Master an ancient and powerful form of magic", "Reunite with a long-lost sibling", 
        "Avenge the wrongful death of a loved one", "Become the best in their chosen field or profession", "Navigate and survive a post-apocalyptic world", 
        "Break a curse that has haunted their lineage for generations", "Build a successful business from scratch", "Explore uncharted territories and discover new worlds", 
        "Protect a coveted secret from falling into the wrong hands", "Win a prestigious competition against all odds", "Resolve a deep-seated family conflict", 
        "Invent something that changes the course of history", "Escape from a life of poverty and hardship", "Find true love in an unexpected place", 
        "Redeem themselves from a major mistake or crime", "Communicate and make peace with an alien species", "Break free from a controlling or abusive relationship", 
        "Restore their honor after being falsely accused", "Survive a journey through a perilous wilderness", "Solve a complex and ancient mystery", 
        "Become a renowned artist, musician, or writer", "Lead a revolution against an oppressive system", "Find inner peace and enlightenment", 
        "Protect a rare and endangered species", "Overcome a debilitating fear or phobia", "Navigate the complexities of court politics and intrigue", 
        "Find a way back home after being stranded far away", "Learn the true meaning of friendship and loyalty", "Make amends for past wrongdoings and find redemption", 
        "Break down social barriers and bring about change", "Survive a brutal and unjust prison sentence", "Confront and defeat a powerful and malevolent force", 
        "Discover the secret to immortality", "Become a leader and role model in their community", "Forge a legendary weapon or artifact", 
        "Rise from obscurity and become a celebrated hero", "Navigate a political conspiracy and come out unscathed", "Prove their worth in a society that undervalues them", 
        "Reclaim their rightful throne or position", "Survive and adapt in a rapidly changing world", "Decode an ancient prophecy and prevent its ominous outcome", 
        "Build a new life in a foreign land", "Heal from a traumatic experience and find strength", "Balance the demands of power with personal morals", 
        "Uncover a hidden talent or ability within themselves", "Bring together a divided community or family"
        #Neutral or morally ambiguous goals
        "Stop the neighbor from making noise", "Get some sleep", "Win a bet no matter the cost", "Secure a promotion by any means necessary", 
        "Sabotage a rival's success subtly", "Hide a secret from a close friend", "Borrow something without asking", "Avoid responsibilities to have fun", 
        "Manipulate a situation to their advantage", "Get out of a tedious task", "Snoop into someone else's affairs", "Keep a valuable find rather than returning it", 
        "Gain fame without working hard for it", "Outsmart the law for personal gain", "Infiltrate a group to learn their secrets", "Convince someone to do their bidding", 
        "Get revenge for a minor slight", "Gain control over a situation through deceit", "Obtain a rare item, regardless of the means", "Cut corners to finish a project", 
        "Get even with a coworker", "Lie to protect their own interests", "Cheat in a game or contest", "Evade taxes or other financial obligations", 
        "Manipulate information for personal benefit", "Use flattery to get what they want", "Ignore rules that they find inconvenient", "Feign illness to avoid an event", 
        "Exploit a loophole for personal gain", "Spy on neighbors or colleagues", "Take credit for someone elses work", "Use someones weakness to their advantage", 
        "Blame others for their own mistakes", "Pretend to be someone theyre not", "Steal a friends idea and claim it as their own", "Break a promise if it benefits them", 
        "Play both sides in a conflict", "Hide their true intentions", "Use emotional manipulation to get their way", "Prioritize their comfort over others needs", 
        "Create a false identity online", "Take advantage of a friend's generosity", "Bend the truth to make a story more interesting", "Sabotage someones plans discreetly", 
        "Collect a debt relentlessly", "Influence others to make a risky decision", "Fake an interest to gain favor", "Use charm to avoid consequences", "Gamble with high stakes", 
        "Bargain aggressively to get a better deal"
        #Negative goals
        "Seize control of a kingdom through treachery", "Steal a powerful artifact to gain supreme power", "Manipulate a war for personal gain", 
        "Destroy a rival's reputation completely", "Conquer neighboring lands mercilessly", "Build a weapon of mass destruction", 
        "Assassinate a political figure for chaos", "Create a monopoly over a vital resource", "Enslave a population for labor", "Unleash a deadly virus on a city", 
        "Blackmail high-ranking officials", "Corrupt a hero to the dark side", "Conduct unethical experiments for knowledge", "Summon a demonic entity for power", 
        "Eradicate a specific group or race", "Steal the identity of someone powerful", "Manipulate the stock market for riches", "Poison a city's water supply", 
        "Betray their country for enemy forces", "Kidnap someone for a hefty ransom", "Frame an innocent person for a crime", "Create an army of mind-controlled soldiers", 
        "Sell state secrets to hostile entities", "Incite a rebellion for political upheaval", "Forge alliances with dark forces", "Use sorcery to control minds", 
        "Destroy a sacred land for resources", "Plot the overthrow of a government", "Siphon the life force of others", "Spread lies and propaganda", 
        "Hack into secure networks for espionage", "Commit acts of terrorism to instill fear", "Usurp the throne through murder", "Traffic forbidden magical artifacts", 
        "Trap souls for eternal servitude", "Instigate a coup to grab power", "Create a cult to worship them", "Manipulate natural disasters for chaos", 
        "Steal rare and powerful technology", "Enact a curse on an enemy's lineage", "Use necromancy for an undead army", "Manipulate time for personal gain", 
        "Sabotage peace talks to continue war", "Release monsters into populated areas", "Orchestrate a heist of national treasures", "Use alchemy for forbidden transformations", 
        "Spread a plague to weaken nations", "Brainwash youth to serve their cause", "Stoke conflicts between powerful factions", "Seek immortality at the cost of lives"
        #Good and rare goals
        "Revive a dying language to preserve cultural heritage", "Restore an ancient monument to honor history", "Create a sanctuary for endangered animals", 
        "Develop a sustainable farming method for arid regions", "Invent a non-polluting energy source", "Establish a scholarship fund for underprivileged students", 
        "Mediate a long-standing border dispute peacefully", "Rescue animals from illegal trafficking", "Restore sight to the blind through innovative surgery", 
        "Initiate a program to clean ocean plastics", "Found a non-profit for mental health awareness", "Translate and publish forgotten literary works", 
        "Rehabilitate a coral reef damaged by pollution", "Set up a free clinic in a remote area", "Launch a campaign to support local artisans", 
        "Create a community garden in an urban food desert", "Organize a relief effort for disaster-stricken areas", 
        "Develop an app to help people with disabilities navigate cities", "Start a cultural exchange program to foster understanding", 
        "Invent an affordable water purification device", "Set up a fund to preserve indigenous art", "Organize a peace concert in a conflict zone", 
        "Initiate a program to reintegrate ex-convicts into society", "Campaign for the rights of gig economy workers", "Establish a wildlife corridor to protect migrating species", 
        "Create a documentary series on unsung heroes of history", "Develop a therapy program using art for trauma victims", "Fund research for a rare genetic disorder", 
        "Revitalize a town's economy through eco-tourism", "Start a mentorship program for aspiring young leaders", "Launch a mobile library for rural communities", 
        "Organize a charity marathon for cancer research", "Set up a network for emergency food distribution", "Champion the cause of renewable energy in policymaking", 
        "Design an eco-friendly urban transportation system", "Create a social movement to reduce food waste", "Organize a series of workshops on financial literacy for teens", 
        "Establish a free legal aid service for the marginalized", "Develop a program to train therapy animals for hospitals", "Launch an initiative to plant a million trees", 
        "Set up a cultural festival to celebrate diversity", "Organize a fundraiser to support local theaters", "Build a playground accessible to children of all abilities", 
        "Start a community initiative to support the elderly", "Fund the restoration of a historic public park", "Develop a sustainable beekeeping project to support biodiversity", 
        "Create a program to teach coding to underrepresented groups", "Set up a network of support for small organic farmers", 
        "Launch a campaign to end single-use plastics in a city"
        #Future goals
        "Integrate advanced AI into their brain for enhanced cognition", "Achieve digital immortality by uploading their consciousness", 
        "Invent a biohacking kit for self-directed evolution", "Establish the first human colony on Mars", "Develop a symbiotic relationship with an alien species", 
        "Create a virtual reality universe indistinguishable from reality", "Engineer a photosynthetic skin for energy sustainability", 
        "Lead an expedition to terraform a new planet", "Invent nanobots for cellular repair and longevity", "Master telepathic communication through neural implants", 
        "Pioneer the use of quantum entanglement in teleportation", "Design a habitat for living in deep space", "Achieve perfect memory recall with a neural lace", 
        "Explore the depths of a gas giant in a custom-built suit", "Found a society based on collective consciousness", "Develop a method for interstellar travel", 
        "Create a personal AI companion with human emotions", "Build a self-sustaining ecosystem on a space station", 
        "Invent a language for communicating with extraterrestrial life", "Become an ambassador for Earth in intergalactic councils", 
        "Design a body that can adapt to any environmental conditions", "Establish a virtual reality school for off-world education", 
        "Create a network of wormholes for instant travel", "Develop a serum for rapid regeneration of tissues", "Construct a megastructure around a star for energy harnessing", 
        "Engineer a bio-luminescent form of human skin", "Invent a time dilation device for space travel", "Start a movement for ethical transhumanism", 
        "Build an artificial planet as a new habitat for humanity", "Discover a method for controlling gravity", "Create a shared consciousness network", 
        "Lead an intergalactic archaeological expedition", "Engineer a way to breathe underwater using gill implants", "Develop a hyperspace communication system", 
        "Create a synthetic ecosystem for extinct Earth species", "Found a colony in an alternate dimension", "Invent a way to harvest energy from black holes", 
        "Establish a peace treaty with a hostile alien race", "Design a nanoscale factory for material synthesis", "Create a wearable device for personal space travel", 
        "Develop a method to reverse the aging process", "Invent a universal translator for all known languages", "Build a museum showcasing the history of the universe", 
        "Engineer plants that can grow on other planets", "Start an interstellar trade network", "Design a suit that adapts to any planetary environment", 
        "Discover a cure for a galactic-scale epidemic", "Create a sentient AI to govern a space colony", "Develop a technology to manipulate dark matter", 
        "Establish a network of floating cities in Jupiter's atmosphere"
        #Negative future goals
        "Exploit alien species for illegal biotechnological advancements", "Monopolize water resources on a colonized planet", 
        "Hack into neural networks to control people's thoughts", "Create a private army of genetically engineered super soldiers", 
        "Blackmail governments using sensitive information from cybernetic implants", "Manipulate the stock market with quantum computing", 
        "Steal terraforming technology to create a private planet", "Spread a computer virus in a global neural network", 
        "Engage in illegal time manipulation for personal gain", "Conduct inhumane experiments in pursuit of immortality", 
        "Control the supply of a vital new energy source", "Build a weaponized space station capable of destroying planets", 
        "Create a monopoly over a new form of interstellar travel", "Enslave an off-world colony for resource extraction", "Sabotage rival colonies' life-support systems", 
        "Trade in illegal memories and experiences in virtual reality", "Establish a dictatorship over a network of colonized worlds", 
        "Use biohacking to create a race of subservient beings", "Exploit quantum entanglement for espionage and theft", 
        "Manipulate the genetics of a population to control their attributes", "Orchestrate the collapse of a rival space federation", 
        "Use advanced AI for orchestrating large-scale cyber warfare", "Corrupt the AI governance of a utopian society", 
        "Steal identities through advanced brain-computer interfaces", "Engineer a virus capable of infecting both biological and cybernetic organisms"
    ]

story_elements["CHARACTER_RACE"] = ["human", "human", "human", "bio-hacked human", "human with animal abilities", "cyborg", 
    ]

story_elements["CHARACTER_AGE"] = ["Child (8 - 12)",
        "Young Adult (13 - 17)",
        "College Age Adult (18 - 25)",
        "Young Working Adult (26 - 35)",
        "Working Adult (36 - 45)",
        "Older Working Adult (46 - 65)",
        "Retiree (66 - 74)",
        "Elderly (75 - 110)",
        "Genetically enhanced (110+)"
    ]

story_elements["CHARACTER_RELATIONSHIP"] = ["Siblings", "Single (happy)", "Single (searching)", "Single (cynical)", "Single (heartbroken)", "Single (playing the field)", "Co-workers (Unacquainted)",
        "Co-workers (close platonic relationship)", "Co-workers (supervisor-supervisee)", "Co-workers (secret lovers)", "Co-workers (rivals)", "Co-workers (enemies)", "Friends",
        "Childhood friends", "Best friends", "Distant friends", "Online only friends (never met in person)", "In a relationship (just started dating)", "In a long term relationship",
        "Fracturing relationship", "Sex only relationship", "Ex-partners", "Engaged", "Married (happily)", "Newlyweds", "Married (unhappy)", "Married (with kids)", "Married (open marriage)",
        "Divorced (happily)", "Divorced (unhappily)", "Divorced (with kids)", "Re-married", "Widow/Widower", "Parasocial relationship", "In a relationship with a higher power/organization",
        "In a relationship with work"
    ]

story_elements["PHYSICAL_BUILD"] = [
    "thin",
    "average",
    "athletic", "angular", "feminine", "narrow", "graceful",
    "competitive athlete build", "plump", "round", "slender",
    "Overweight",
    "Obese"
]

story_elements["Tone_of_voice"] = ["Cheerful", "Melancholy", "Monotone", "Gruff", "Sincere", "Sarcastic", "Whiny", "Enthusiastic", "Apathetic", "Cold"]

story_elements["LANGUAGE_TYPE"] = ["Articulate", "Inarticulate", "Profane", "Academic", "Simple", "Flowery", "Technical"]

story_elements["CLOTHING_STYLE"] = [
    "artistic", "attractive", "bizarre", "businesslike", "classy", 
    "complicated", "dignified", "elaborate", "elegant", "flattering",
    "impractical", "mysterious", "no-nonsense", "odd", "plain", 
    "practical", "professional", "revealing", "risque", "severe",
    "sexy", "simple", "strange", "tight", "uncomplicated", 
    "unconventional", "unusual", "utilitarian", "weird"
]

story_elements["BIRTHPLACE"] = ["A bustling city", "A remote village", "The depths of a forest", "A small island", "The heart of a desert", "A mountain village", "The edge of an ocean",
    "The streets of a metropolis", "A high-tech space station", "A quiet suburb", "The frozen tundra", "A lush valley", "An ancient castle", "A nomadic tribe", "Aboard a sailing ship",
    "A secluded monastery", "The underground tunnels", "A thriving coastal town", "A futuristic city", "A war-torn country", "An enchanted forest", "A floating city in the sky",
    "A traditional farmstead", "The ruins of an ancient civilization", "A bustling market town", "A hidden jungle village", "The expansive prairie", "A luxurious palace", "A remote research station",
    "An industrial complex", "The slums of a city", "A mystical mountain peak", "A forgotten ghost town", "The depths of the ocean", "A colony on the moon", "A nomadic caravan",
    "An artist's commune", "A rebel base", "The backstage of a theater", "A scholarly library", "An alien planet", "A high-rise apartment in a city", "A camp in the wilderness",
    "A bustling harbor", "The corridors of power", "An underground bunker", "A quaint coastal village", "The rooftops of a city", "A traveling circus", "A frontier outpost",
    "Aboard an interstellar ark", "An underwater city", "Inside a volcano's dormant crater",
    "A floating monastery in the Himalayas",
    "A sky city suspended by balloons",
    "A labyrinth beneath an ancient city",
    "An isolated research facility in Antarctica",
    "A hidden valley of dinosaurs",
    "An eco-village in the Amazon rainforest",
    "A colony inside a massive asteroid",
    "An ancient temple in a dense jungle",
    "A town where it's always night",
    "A city built on the back of a giant creature",
    "An oasis in the midst of a mirage",
    "A secret society's underground city",
    "A village on a floating island in the sky",
    "A settlement at the earth's core",
    "An enchanted castle floating in the clouds",
    "A fortress on the edge of a black hole",
    "A town inside a massive cave system",
    "A city hidden inside a giant waterfall",
    "A pirate haven on a hidden archipelago",
    "A town that travels through time",
    "A village where magic is real",
    "An abandoned space colony on Mars",
    "A ghost town reclaimed by nature",
    "A nomadic tribe in a glass desert",
    "A sanctuary city for supernatural beings",
    "A secret base in the Arctic Circle",
    "A city built within a colossal tree",
    "A utopia in an alternate dimension",
    "An ancient library buried beneath the sands",
    "A town perpetually in autumn",
    "A space elevator's base station",
    "A civilization inside a biosphere",
    "A floating city powered by steam",
    "A hidden academy for spies",
    "An enchanted village that changes location",
    "A city in a bubble under the sea",
    "A mystical shrine on a mountain peak",
    "An art commune in a repurposed fortress",
    "A settlement on the dark side of the moon",
    "A town where everyone can fly",
    "A city built around a sleeping dragon",
    "A futuristic metropolis in a parallel universe",
    "An ancient ruin floating in space",
    "A village cursed to eternal twilight",
    "An outpost at the end of the galaxy",
    "A city where history and future merge",
    "A hidden kingdom in a valley of giants",
    "A city recovering from an epidemic",
    "A village recently hit by a natural disaster",
    "A country undergoing a revolution",
    "A community in the midst of a famine",
    "A town isolated by a massive snowstorm",
    "An area evacuated due to a nuclear accident",
    "A region ravaged by a prolonged drought",
    "A city under martial law",
    "A community living under a strict theocracy",
    "A village coping with a supernatural curse",
    "An area affected by extreme pollution",
    "A city experiencing a technological boom",
    "A community suffering from economic collapse",
    "A country divided by civil war",
        "A town haunted by a historical tragedy",
    "A region experiencing unprecedented immigration",
    "A city at the forefront of a cultural renaissance",
    "A village that has rediscovered ancient technology",
    "An area in the throes of a gold rush",
    "A country facing a critical water shortage",
    "A city rebuilding after a major earthquake",
    "A community threatened by a looming volcano",
    "A society transitioning from dictatorship to democracy",
    "A region caught in the crossfire of warring factions",
    "A city that has become a hub for espionage",
    "A village experiencing a religious awakening",
    "A country in the grip of a coup d'état",
    "A community affected by a bizarre scientific experiment",
    "A region under the threat of an alien invasion",
    "A city in the middle of a housing crisis",
    "A village plagued by a mysterious illness",
    "A country suffering under economic sanctions",
    "A town on the verge of a technological singularity",
    "A community facing the impact of climate change",
    "A society where artificial intelligence governs",
    "A region dealing with the aftermath of a cyber attack",
    "A city where virtual reality is more common than reality",
    "A community torn apart by a divisive referendum",
    "A country recovering from a terrorist attack",
    "A village cut off by a border conflict",
    "An area experiencing a severe energy crisis",
    "A city transformed by a cultural movement",
    "A society adapting to life after a pandemic",
    "A region where time travel has disrupted society",
    "A community struggling with the ethics of genetic engineering",
    "A city in the midst of a media frenzy",
    "A village that has become a tourist attraction against its will",
    "A country facing a major demographic shift",
    "A town where a historical discovery has changed everything",
    "A society learning to live with newly discovered creatures",
    "A city floating in a bubble through interstellar space",
    "A civilization inside a living organism",
    "A village where time flows backwards",
    "An underwater realm where memories can be physically visited",
    "A community living on the wings of a giant, flying creature",
    "A city where buildings constantly reshape themselves",
    "A society existing within a colossal hourglass",
    "A town on a planet where the laws of physics don't apply",
    "A village in a world where colors are sentient",
    "A city suspended in a perpetual eclipse",
    "An island floating in the sky, tethered to the Earth by chains",
    "A community inside a giant, hollowed-out comet",
    "A society in a realm where dreams and reality merge",
    "A city built on a tapestry of interwoven dimensions",
    "A village where each inhabitant is a different species of intelligent plants",
    "A city inside a bubble on the surface of the sun",
    "A community living in the reflection of a giant mirror",
    "An ancient civilization on a planet of endless waterfalls",
    "A village in a world where sound creates physical shapes",
    "A city inside a pocket dimension with inverted gravity",
    "A society on a world where shadows have a life of their own",
    "A town on a planet with a liquid sky",
    "A village where inhabitants can morph their physical form at will",
    "A city floating on a sea of glass above an endless abyss",
    "An island where each day brings a completely new ecosystem",
    "A community living on a world-sized, sentient tree",
    "A society inside a crystal orb orbiting a black hole",
    "A town in a universe where each individual creates their own laws of nature",
    "A village on a planet where night never falls",
    "A city built within a giant, intergalactic clockwork mechanism",
    "An underwater city in a sea of liquid light",
    "A society where each thought manifests as physical reality",
    "A community living in the core of a planet-sized diamond",
    "A village in a dimension where time is a tangible substance",
    "A city on a planet with rings of woven energy",
    "An enclave in a realm of eternal twilight, lit by bioluminescent life",
    "A town on a fragment of a shattered planet, held together by unknown forces",
    "A society in a cosmic kaleidoscope",
    "A village where every building is a living creature",
    "A city in a world where weather is controlled by emotions",
    "A community on a planet where natural landscapes are geometric",
    "A civilization within a giant, orbiting terrarium",
    "A society on a world with a fragmented, puzzle-piece landmass",
    "A town in a dimension where sound is visible and light is audible",
    "A village on a planet where the sea and sky switch places daily",
    "A city inside a giant, ancient automaton",
    "An island in a sea of swirling, solid air",
    "A community living on a tapestry of interconnected mini-worlds",
    "A town in a realm where historical eras coexist simultaneously",
    "A civilization on a fragment of reality drifting through a void of possibilities"
]

story_elements["LIFE_SATISFACTION"] = [
    "miserable", 
    "Very Unhappy", 
    "Unhappy", 
    "Slightly Unsatisfied", 
    "Neutral", 
    "Slightly Satisfied", 
    "Content", 
    "Happy", 
    "Very Happy", 
    "Almost Perfect!"
]

story_elements["MENTAL_HEALTH_STATUS"] = [
    "Borderline Suicidal", 
    "Severely Depressed",
    "Depressed",
    "Anxious",
    "Average",
    "Mentally Stable",
    "Well-adjusted",
    "Optimistic",
    "Highly Resilient",
    "Perfectly balanced"
]

story_elements["PHYSICAL_HEALTH_STATUS"] = [
    "Frail, Possibly Disabled",
    "Chronically Ill",
    "Frequently Unwell",
    "Below Average",
    "Average",
    "Fit",
    "Very Fit",
    "Athletic",
    "Exceptionally Healthy",
    "Excellent Health"
]

story_elements["FINANCIAL_HEALTH_STATUS"] = [
    "Poor",
    "Struggling",
    "Financially Stressed",
    "Making Ends Meet",
    "Average",
    "Comfortable",
    "Well-off",
    "Financially Secure",
    "Affluent",
    "Wealthy"
]

story_elements["PERSONAL_MOTIVATION"]= [
    "Survival",
    "Revenge",
    "Love",
    "Family",
    "Recognition",
    "Power",
    "Wealth",
    "Redemption",
    "Freedom",
    "Knowledge",
    "Legacy",
    "Justice",
    "Adventure",
    "Self-Improvement",
    "Competition",
    "Duty",
    "Fear",
    "Friendship",
    "Loyalty",
    "Curiosity",
    "Peace",
    "Chaos",
    "Altruism",
    "Creativity",
    "Validation",
    "Belonging",
    "Fame",
    "Independence",
    "Exploration",
    "Challenge",
    "Religion/Spirituality",
    "Moral Integrity",
    "Ambition",
    "Pleasure",
    "Conquest",
    "Recognition within Subculture",
    "Escapism",
    "Tradition",
    "Rebellion",
    "Preservation",
    "Jealousy",
    "Health",
    "Equality",
    "Control over Destiny",
    "Anonymity",
    "Legacy for Offspring",
    "Patriotism",
    "Personal Growth",
    "Nostalgia",
    "Retribution",
    # "More motivations" seems to be an instruction rather than an item in the list
]

story_elements["CHARACTER_STRENGTH"] = [
        "Resilience", "Empathy", "Intelligence", "Courage", "Loyalty", "Honesty", 
        "Compassion", "Optimism", "Integrity", "Creativity", "Discipline", "Initiative", 
        "Leadership", "Adaptability", "Confidence", "Charisma", "Patience", "Perseverance", 
        "Wit", "Ambition", "Altruism", "Open-mindedness", "Gratitude", "Self-awareness", 
        "Humility", "Focus", "Determination", "Cooperation", "Kindness", "Resourcefulness", 
        "Accountability", "Skillfulness", "Assertiveness", "Passion", "Tolerance", 
        "Generosity", "Pragmatism", "Visionary", "Empowerment", "Spontaneity", "Dedication", 
        "Discretion", "Insightfulness", "Curiosity", "Mindfulness", "Foresight", "Sincerity", 
        "Tenacity", "Diligence", "Forgiveness"
    ]

story_elements["CHARACTER_WEAKNESS"] = [
    "Arrogance", "Impulsiveness", "Greed", "Dishonesty", "Cowardice", 
    "Insecurity", "Short-Temperedness", "Jealousy", "Procrastination", 
    "Stubbornness", "Laziness", "Indecisiveness", "Ignorance", "Gullibility", 
    "Overconfidence", "Apathy", "Intolerance", "Naivety", "Selfishness", 
    "Manipulative", "Recklessness", "Vengefulness", "Perfectionism", "Vanity", 
    "Close-mindedness", "Pessimism", "Insensitivity", "Hypocrisy", "Dependence", 
    "Sycophancy", "Impatience", "Materialism", "Inconsistency", "Forgetfulness", 
    "Melancholy", "Paranoia", "Cynicism", "Absent-mindedness", "Pettiness", 
    "Fanaticism", "Excessive Pride", "Escapism", "Disloyalty", "Moodiness", 
    "Skepticism", "Indifference", "Ingratitude", "Overcompetitiveness", 
    "Unreliability", "Deceptiveness", "Low self-esteem"
]

story_elements["CHARACTER_SECRET"] = [
        "I'm adopted but I've never told anyone.",
        "I cheated on an important exam in high school.",
        "I'm still in love with my ex.",
        "I have a secret half-sibling my family doesn't know about.",
        "I never actually graduated from college like I tell people.",
        "I caused the injury that ended my friend's sports career.",
        "I've stolen money from jobs in the past.",
        "I frequently call in sick when I'm not really ill.",
        "I once ran a red light and caused an accident but drove away.",
        "I pretended to have a terminal illness to get money from friends.",
        "I lied about my credentials to get my current job.",
        "I'm secretly addicted to prescription painkillers.",
        "I cheated with my best friend's partner.",
        "I have a hidden social media account to stalk exes.",
        "I used to deal drugs and launder money.",
        "I got plastic surgery but tell people I look this good naturally.",
        "I write fake positive reviews for my own business.",
        "I've borrowed money I can't repay from friends and family.",
        "I have an illegitimate child I keep secret.",
        "I never finished my master's degree like I claim.",
        "I started the nasty rumor that ruined my coworker's career.",
        "I have a criminal record under a different name.",
        "I'm embellishing my past to run for public office.",
        "I filed for bankruptcy years ago but kept it quiet.",
        "I lied about my age to marry someone much younger.",
        "I cheated my way through college with paid test takers.",
        "I'm secretly struggling with a severe gambling addiction.",
        "I maintain multiple social media accounts to manipulate people.",
        "I frequently abuse prescription drugs recreationally.",
        "I started the fire that burned down my childhood home for insurance money.",
        "I've stolen business ideas from past employers and claimed them as my own.",
        "I keep secrets about my sexuality that would shock my friends and family.",
        "I never visit my sick relative like I claim - I use that time for myself.",
        "I once injured someone in a hit and run while driving drunk.",
        "I lied that I have a made-up disease to get donations from strangers.",
        "I pretend my family is wealthy but we actually live paycheck to paycheck.",
        "I'm having an affair with a married coworker.",
        "I swindled my last employer out of thousands before getting fired.",
        "I have multiple identities and backstories I use to manipulate people.",
        "I hacked into a company's system and stole proprietary information to advance my career.",
        "I secretly despise my spouse but keep up happy appearances.",
        "I never graduated high school like I claim.",
        "I started malicious rumors about a former boss who fired me.",
        "I take credit for other people's work and ideas.",
        "I exploited tax loopholes to avoid paying what I owe.",
        "I'm a top member of an online hate group using a fake identity.",
        "I lied about my military service - I was never actually deployed.",
        "I pretend to be a victim of a violent crime for sympathy and donations.",
        "I frequently post fake positive stories about myself online.",
        "I have a hidden camera in someone else's home.",
        "I'm still secretly in love with a childhood sweetheart who is now married.",
        "I never graduated from the prestigious university I claim to have attended.",
        "I started an anonymous blog detailing all my coworkers' secrets that got someone fired.",
        "I pretended to be disabled to win a huge settlement in a fraudulent lawsuit.",
        "I cheated my way to winning a major competition years ago.",
        "I secretly hate one of my children but pretend to love them equally.",
        "I'm seeing a therapist for violent thoughts I haven't shared with anyone.",
        "I plagiarized most of the work that launched my successful career.",
        "I pressured someone into having an abortion so I wouldn't have to pay child support.",
        "I stole thousands from past roommates by overcharging rent.",
        "I catfish people online using fake identities.",
        "I started seeing my best friend's recent ex-partner behind their back.",
        "I lied about founding a charity - I just collect donations for myself.",
        "I have a hidden food addiction I go to great lengths to keep secret.",
        "I'm acting happy but I'm suicidal and have a detailed plan.",
        "I hacked into a celebrity's social media and leaked private information for money.",
        "I secretly record private conversations and blackmail people with them.",
        "I pretended to need an organ transplant to solicit donations I kept.",
        "I stole money from my last three partners.",
        "I had an affair with my boss to get promoted at my old job.",
        "I sabotaged a teammate's career because I was jealous of their success.",
        "I leaked company secrets to damage their stock price for personal profit.",
        "I lied about my credentials - I never actually have the medical degree I claim.",
        "I destroyed evidence and lied to police to help a guilty relative avoid conviction.",
        "I married for money and pretend to love someone I can't stand.",
        "I secretly despise a disabled family member but act like a loving caretaker.",
        "I once injured an athlete to manipulate betting odds and win big.",
        "I pretended to be a victim of discrimination to sue an employer and settle out of court.",
        "I steal pets and ransom them back to devastated owners.",
        "I hid my criminal past and changed my name before pursuing public office.",
        "I abused positions of power at past jobs to sexually exploit subordinates.",
        "I secretly hate popular people and sabotage them behind their backs.",
        "I lied that a deceased relative left me a fortune - I actually have crippling debt.",
        "I pretend to be progressive but have hatred and prejudices I keep hidden.",
        "I swipe office supplies and sell them online for extra income.",
        "I maintain an alter ego and second life unbeknownst to anyone who knows me.",
        "I poisoned someone's pet when it wouldn't stop barking.",
        "I secretly use dark magic and spells that would disturb others if they knew.",
        "I'm secretly a government spy using this mundane identity as a cover.",
        "I leaked private photos of a celebrity I hacked to damage their reputation.",
        "I spew hate speech anonymously online but publicly pretend to be open-minded.",
        "I secretly have children nobody knows about.",
        "I caused a friend's suicide but pretended to be devastated when they died.",
        "I'm syphoning company funds into a secret offshore account.",
        "I maintain multiple fabricated personas online for manipulation.",
        "I lied about my ethnicity to take advantage of affirmative action and scholarships.",
        "I hunted people for sport on the dark web.",
        "I pretend to be pious but have violently blasphemous thoughts.",
        "I maintain an anonymous account where I bully friends and strangers.",
        "I'm slowly poisoning a relative to inherit money sooner.",
        "I'm plotting to overthrow the government and rule the country.",
        "I experiment on animals in my basement for fun.",
        "I belong to a secret society that performs occult rituals.",
        "I robbed my family and disappeared to start a new life with the money.",
        "I maintain a hidden second family no one knows about.",
        "I poisoned my mentor to take over the business for myself.",
        "I'm a spy selling classified secrets to enemy governments.",
        "I secretly despise the culture I publicly promote and represent.",
        "I embezzled millions from charities I championed to fund my lavish lifestyle.",
        "I destroyed my rivals' careers through malicious rumors and blackmail.",
        "I shot someone and framed an innocent person who went to prison for it.",
        "I started a cult and brainwash followers for money and power.",
        "I experiment on homeless people without consent.",
        "I murdered someone and disposed of the body, but nobody ever found out.",
        "I have a collection of macabre souvenirs from murders I got away with.",
        "I manipulated disadvantaged people into committing crimes for me.",
        "I poisoned someone slowly over many months and pretended to comfort them as they declined.",
        "I maintain multiple identities in different countries as part of a complex con.",
        "I secretly run exotic animal fights for high stakes gambling.",
        "I stole artifacts and sold them on the black market to fund my lifestyle.",
        "I hacked major corporations to manipulate stock prices for personal profit.",
        "I poisoned someone's enemies and charged them for it.",
        "I secretly run an evil empire built on the backs of the oppressed.",
        "I intentionally cause disasters to profit from rebuilding efforts.",
        "I sabotaged peace talks between warring nations to prolong the conflict.",
        "I leaked state secrets and caused a lot of damage to public trust and national security.",
        "I traffic forbidden substances disguised as harmless shipments.",
        "I engineered a pathogen in my home lab that could start a deadly pandemic.",
        "I shot down a passenger jet to assassinate a political refugee.",
        "I secretly started the doomsday cult planning a mass suicide.",
        "I stole massive amounts of wealth and framed innocent people for the crime.",
        "I manipulate elections and public opinion through targeted misinformation campaigns.",
        "I clandestinely sell weapons to unstable regimes.",  "I burned down low-income housing to drive out unwanted groups.",
        "I brutally repress protestors campaigning for justice and democracy.",
        "I run a poaching operation that's driving endangered species to extinction.",
        "I profit off human trafficking and exploit the poor and vulnerable.",
        "I swindle elderly people out of their retirement savings.",
        "I secretly test chemical weapons on civilian populations.",
        "I launder money and provide financial services to dangerous criminals.",
        "I own politicians and subvert democracy to serve my own interests.",
        "I started conflicts between nations that resulted in countless lives lost.",
        "I manipulated impressionable young people into throwing their lives away for my cause.",
        "I pretend to be concerned about inequality while hoarding staggering wealth.",
        "I publicly call for sustainability while profiting from pollution and environmental destruction.",
        "I've ruined people's lives with false accusations in the name of a greater cause.",
        "I exploited slave labor to amass my wealth.",
        "I orchestrated hate crimes to fuel divisions and make profit from chaos.",
        "I have participated in atrocities that would be considered war crimes.",
        "I planned the assassination of a world leader."
    ]

story_elements["CHARACTER_MEGA_ARCHETYPE"] = [
    "The Hero: Often an unlikely candidate who rises to the occasion",
    "The Mentor: A wise figure who guides the hero",
    "The Threshold Guardian: Entities that challenge or block the hero’s path",
    "The Herald: Brings the call to adventure",
    "The Shapeshifter: Characters whose loyalties or identities are uncertain",
    "The Shadow: Represents the darker aspects, often the antagonist or the hero’s inner conflicts",
    "The Trickster: A mischievous figure or comic relief that also challenges the status quo"
]

story_elements["Character_sub-archetype"] = [
    "The Rogue With a Heart of Gold: Seemingly selfish or aloof, this character eventually reveals a deep sense of honor and willingness to risk all for the right cause. Example: Han Solo from Star Wars",
    "The Rebellious Hero: Rejects societal norms and bravely defies authority, driven by a deeper understanding or morality that others might not see. Example: Aragorn from The Lord of the Rings",
    "The Disguised Stranger: Someone who hides their true identity, often revealing themselves in a pivotal moment, providing a dramatic twist to the story. Example: Katniss Everdeen from The Hunger Games",
    "The Wandering Bard: Roaming from place to place, this character is both a teller of tales and a player in them, often influencing events subtly. Example: Kvothe from The Name of the Wind",
    "The Broken Optimist: Once believed in the best outcomes, but life events have jaded them, setting them on a path to regain their optimism. Example: Ted Lasso from Ted Lasso",
    "The Gentle Giant: Imposing in stature but soft at heart, their physical strength is in contrast with their gentle nature. Example: Hodor from Game of Thrones",
    "The Reluctant Warrior: Prefers peace and avoids conflict, but when pushed, displays unmatched skill and determination in combat. Example: Samwise Gamgee from The Lord of the Rings",
    "The Seeker of Vengeance: Motivated primarily by revenge, their journey often questions the costs and morality of their quest. Example: Inigo Montoya from The Princess Bride",
    "The Cursed Wanderer: A character doomed to roam, often bearing a curse or a tragic past that denies them rest or respite. Example: The Flying Dutchman",
    "The Melancholic Dreamer: Often lost in thought, this archetype is more in tune with the ethereal and the artistic, sometimes to their detriment. Example: Jay Gatsby from The Great Gatsby",
    "The Enigmatic Scholar: Holds vast knowledge and is often reserved, revealing depths in carefully chosen moments. Example: Trelawney from Harry Potter",
    "The Fallen Hero: Once revered but brought down by a flaw or twist of fate, their journey is one of redemption or tragedy.  Example: Anakin Skywalker from Star Wars",
    "The Scheming Artisan: Talented in their craft but uses it for dubious or malicious ends, weaving complex plots. Example: Iago from Othello",
    "The Leader with a Dark Secret: Exudes confidence and gathers followers, but hides a crucial aspect of their past or intentions. Example: President Snow from The Hunger Games",
    "The Outlaw Out for Justice: Operates outside the law, but for noble or just causes, often challenging what's deemed 'legal' and 'moral'. Example: Robin Hood.",
    "The Silent Observer: Speaks little, but their actions or the few words they do utter hold significant weight or insight. Example: Boo Radley from To Kill a Mockingbird",
    "The Ethereal Mystic: Connected deeply with the spiritual or supernatural, their knowledge often guides or warns the main characters. Example: The Ancient One from Doctor Strange",
    "The Enigmatic Stranger: Appears unexpectedly, offering assistance or posing challenges, their true intentions and identity a mystery. Example: The Continental Op from Dashiell Hammett's detective stories",
    "The Puppet Master: Operates from the shadows, manipulating events and characters to achieve their goals. Example: Varys from Game of Thrones",
    "The Defiant Artist: Uses their art to challenge norms, make political statements, or rebel against established order. Example: Edmond Dantès from The Count of Monte Cristo",
    "The Nurturing Guardian: Offers emotional, spiritual, or physical protection and guidance, often at the risk of their own well-being. Example: Molly Weasley from Harry Potter",
    "The Dreamer Awakened: Once lived in their own world or fantasies, but a pivotal event forces them to confront reality. Example: Walter Mitty from… The Secret Life of Walter Mitty",
    "The Fallen Noble: Was once in a position of power or prestige but lost it, now seeks redemption or a return to former glory. Example: Prince Zuko from Avatar: The Last Airbender",
    "The Merchant with a Code: Engages in commerce (sometimes illicit), but operates based on a set of unbreakable personal ethics. Example: Han Solo from Star Wars before he joins the Rebellion",
    "The Charming Scoundrel: Engages in morally ambiguous or outright criminal activities but does so with charm and wit. Example: Neal Caffrey from White Collar",
    "The Ethical Adversary: Opposes the protagonist but does so out of personal honor or a conflicting sense of what's right. Example: Killmonger from Black Panther",
    "The Reviled Martyr: Sacrifices for the greater good but receives scorn or indifference rather than praise from the masses. Example: John Proctor from The Crucible",
    "The Mirror Twin: Bears an uncanny resemblance in appearance or character to another, often revealing suppressed traits or desires of the counterpart. Example: Tyler Durden from Fight Club ",
    "The Hopeful Outlander: From a different culture or world, they bring fresh perspectives and optimism, often challenging the status quo. Example: Wonder Woman in… Wonder Woman",
    "The Mournful Avenger: Seeks vengeance for a personal loss, driven by sorrow and rage, often questioning their own motives along the way. Example: The Bride from Kill Bill",
    "The Lighthearted Sage: Imparts wisdom or guidance, but does so with humor and a carefree demeanor. Example: Uncle Iroh from Avatar: The Last Airbender",
    "The Reclusive Genius: Exceptionally skilled or knowledgeable, but shuns society, often due to trauma or disdain for societal norms. Example: Dr Robert Ford from Westworld",
    "The Sentinel at the End: Guards the last barrier or threshold the protagonist must face, often providing the final challenge. Example: The Black Knight from Monty Python and the Holy Grail",
    "The Orphan Seeking Kin: Driven by a desire to find their true origins or family, their journey intertwines with larger events. Example: Elsa from Frozen",
    "The Masked Avenger: Works in the shadows, hiding their identity as they seek justice or vengeance. Example: V from… V for Vendetta",
    "The Wild Card: Unpredictable, with shifting loyalties or unclear motives, they add an element of uncertainty to the story. Example: Tactus from Red Rising",
    "The Naive Idealist: Often young or inexperienced, they believe in the inherent good of the world, which might lead to both triumphs and tragedies. Example: Pip from Great Expectations",
    "The Brooding Loner: Haunted by their past, they prefer solitude but are often pulled into societal affairs against their will. Example: Jessica Jones from… the Jessica Jones series",
    "The Resilient Survivor: Has undergone significant trauma, yet their journey is one of healing and overcoming. Example: Lisbeth Salander from The Girl with the Dragon Tattoo",
    "The Curious Explorer: Driven by a thirst for knowledge or the unknown, they often embark on adventures into uncharted territories. Example: Sir John Huxley from The Lost World",
    "The Playful Trickster: Relies on wit and cunning, often playing pranks or deceiving others, but not necessarily with malicious intent. Example: Puck from A Midsummer Night's Dream",
    "The Aging Warrior: Past their prime but with a wealth of experience, they often play mentor roles or seek one final grand adventure. Example: Master Roshi from Dragon Ball",
    "The Benevolent Guide: Often has mystical or otherworldly knowledge, guiding the protagonist on their journey.  Example: Mr Miyagi from The Karate Kid",
    "The Outcast with a Secret: Shunned or misunderstood by society, they possess knowledge or abilities that become crucial to the plot. Example: Quasimodo from The Hunchback of Notre Dame",
    "The Determined Inventor: Driven by innovation, they're constantly creating, sometimes leading to beneficial discoveries or unintended consequences. Example: Doc Brown from Back to the Future",
    "The Cynic with a Hidden Heart: Appears jaded or sarcastic but eventually reveals deep-seated passion or kindness.  Example: Dr Gregory House from… House",
    "The Guardian at the Crossroads: Protects a certain territory or object, determining who can pass or obtain it, often testing the protagonist's worthiness. Example: The Sphinx from Greek mythology",
    "The Time-Tested Friend: Has been friends with another character for ages, providing a bridge to the past and unconditional support. Example: Sevro in Red Rising",
    "The Wanderer with No Past: Arrives from nowhere, with no past that they're willing to discuss, but plays a crucial role in events. Example: The Man With No Name from A Fistful of Dollars",
    "The Prophet of Doom: Predicts dire events or outcomes, often dismissed or misunderstood until their prophecies begin to come true. Example: Cassandra from Greek mythology",
    "The Relentless Pursuer: Single-minded in their mission to hunt someone or something down, stopping at nothing to achieve their goal. Example: Javert from Les Misérables",
    "The Enthusiastic Amateur: Lacks professional skills or knowledge but makes up for it with passion and a can-do attitude. Example: Elle Woods from Legally Blonde",
    "The Virtuous Outcast: Possesses a moral code but is excluded or shunned by mainstream society. Example: Jean Valjean from Les Misérables",
    "The Disguised Ruler: A leader or royalty in hiding, either for protection or to observe their people unnoticed. Example: King Richard in Robin Hood",
    "The Dreamer Bound by Reality: Aspires for more than their circumstances allow, often leading to bittersweet outcomes.Example: Walter Mitty from The Secret Life of Walter Mitty",
    "The Fallen Mentor: Once a guide or teacher, they've since lost their way, often needing redemption or serving as a warning. Example: Ben Kenobi from Star Wars",
    "The Ambiguous Ally: Their allegiance is unclear, keeping other characters (and the audience) guessing. Example: Severus Snape from Harry Potter",
    "The Pacifist Warrior: Skilled in combat but chooses non-violence, only fighting when absolutely necessary. Example: Aang from Avatar: The Last Airbender",
    "The Altruistic Thief: Steals, but with noble intentions, often redistributing wealth or righting societal wrongs. Example: Robin Hood",
    "The Disillusioned Dreamer: Once held great ideals or dreams but faced setbacks, leading to a more cynical worldview. Example: Don Quixote from… Don Quixote",
    "The Benevolent Conqueror: Seeks to expand their domain, but with the aim of bringing peace, order, or prosperity. Example: Cyrus the Great",
    "The Broken Peacemaker: Strives for peace but has personal traumas or conflicts that they struggle with. Example: Desmond Doss from Hacksaw Ridge",
    "The Seeker of Forbidden Truths: Goes to great lengths to uncover truths that others believe should remain hidden or forgotten. Example: Robert Langdon from Angels & Demons",
    "The Ethical Mercenary: Works for hire, but has a personal code that dictates who they will and won't work for or what jobs they'll accept. Example: Geralt of Rivia from The Witcher",
    "The Tinkerer at the Crossroads: Always inventing or tweaking, their creations might bring about significant change or disaster. Example: Doc Brown from Back to the Future",
    "The Displaced Noble: Born to privilege but finds themselves in humble or challenging circumstances, often learning profound lessons. Example: Prince Edward from The Prince and the Pauper",
    "The Tormented Artist: Creates profound art but is plagued by personal demons or societal misunderstandings. Example: Vincent van Gogh",
    "The Echo from the Past: Returns from a bygone era or brings an old way of thinking into the present, challenging modern perspectives. Example: Captain America in The Avengers",
    "The Defender of the Lost Cause: Continues to fight for a cause that most believe is already lost or futile. Example: Ned Stark from Game of Thrones",
    "The Hidden Mastermind: Operates from the shadows, their influence felt but their identity and intentions concealed. Example: Keyser Söze from The Usual Suspects",
    "The Star-Crossed Lovers: These characters are deeply in love but fated for tragedy, often due to external forces like feuding families, differing backgrounds, or insurmountable circumstances. Example: Romeo and Juliet",
    "The Loyal Retainer: Unwaveringly dedicated to another character, they provide support, often at great personal risk or sacrifice. Example: Alfred from Batman",
    "The Forgotten Chronicler: Records events or truths that others overlook or choose to forget, often providing a different perspective on history. Example: Samwell Tarly from Game of Thrones"
]



# Now, all your categories are formatted and ready for use in your story generator.





def select_random_element(category):
    return random.choice(story_elements[category])

def generate_story():
    story = f"This {select_random_element('NARRATIVE_PERSPECTIVE')} story is about a {select_random_element('CHARACTER_DESCRIPTOR')} {select_random_element('CHARACTER_GENDER')} {select_random_element('MILITARY_PROTAGONIST')} {select_random_element('JOBS')} during {select_random_element('MILITARY_SCENARIO')}. "
    story += f"Their goal is to {select_random_element('CHARACTER_GOALS')}. \n"
    story += f"But {select_random_element('CHARACTER_DESCRIPTOR')} {select_random_element('BASIC_EVENT')} gets in their way. \n\n"
    story += f"The major event of the story involves {select_random_element('BASIC_EVENT')}. "
    story += f"This is a {select_random_element('STORY_DESCRIPTOR')} {select_random_element('STORY_TYPE')}-themed story, "
    story += f"with a {select_random_element('STORY_DESCRIPTOR')} ending. \n\n"
    story += f"It takes place in the {select_random_element('TIME_PERIOD')} in a {select_random_element('world_scopes')} {select_random_element('World_State')} world influenced by {select_random_element('Culture_Inspiration')} culture. \n\n"
    story += f"The piece of technology central to the plot is the {select_random_element('TECHNOLOGY_FUNCTION')} {select_random_element('TECHNOLOGY_OBJECT')}. "
    story += f"This is known to cause {select_random_element('EMOTION_AMPLIFIER')} leading to {select_random_element('EMOTION')}. \n\n"
    story += f"It is also rumored to allow the user the ability of: {select_random_element('SUPERHUMAN_ABILITY')}.\n\n"
    story += f"This story explores the emotion of: {select_random_element('EMOTION')}.\n\n"
    story += f"Elements and themes from the video game {select_random_element('VIDEO_GAME_FRANCHISE')} are adapted in this story.\n\n"
    story += f"The main character is a {select_random_element('CHARACTER_RACE')} {select_random_element('CHARACTER_AGE')}, "
    story += f"their relationship status is {select_random_element('CHARACTER_RELATIONSHIP')}. \n\n"
    story += f"Here are more facts about the main character: \n\n"
    story += f"Physical build: {select_random_element('PHYSICAL_BUILD')} \n\n"
    story += f"Tone of voice: {select_random_element('Tone_of_voice')} \n\n"
    story += f"Language type: {select_random_element('LANGUAGE_TYPE')} \n\n"  
    story += f"Clothing style: {select_random_element('CLOTHING_STYLE')} \n\n"  
    story += f"Birth location: {select_random_element('BIRTHPLACE')} \n\n"
    story += f"Overall life satisfaction: {select_random_element('LIFE_SATISFACTION')} \n\n"
    story += f"Mental health status: {select_random_element('MENTAL_HEALTH_STATUS')} \n\n"
    story += f"Physical health status: {select_random_element('PHYSICAL_HEALTH_STATUS')} \n\n"
    story += f"Financial health status: {select_random_element('FINANCIAL_HEALTH_STATUS')} \n\n"
    story += f"Personal motivation: {select_random_element('PERSONAL_MOTIVATION')} \n\n"
    story += f"Character strength: {select_random_element('CHARACTER_STRENGTH')} \n\n" 
    story += f"Character weakness: {select_random_element('CHARACTER_WEAKNESS')} \n\n" 
    story += f"Character secret: {select_random_element('CHARACTER_SECRET')} \n\n"
    story += f"Mega-archetype: {select_random_element('CHARACTER_MEGA_ARCHETYPE')} \n\n"
    story += f"Sub-archetype: {select_random_element('Character_sub-archetype')} \n\n"  


    return story

# Generate a story
print(generate_story())
