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
        "unremarkable", "unstable", "unwise", "vicious", "violent", "weak", "wealthy", "well-traveled", "wise", "withdrawn", "youthful", "foolish", "vindictive"
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
    "power outage", "blizzard", "tornado", "famine", "dehydration", "pestilience", "pandemic", "inflation", "election",
]


# Example for other categories, following the same structure:
story_elements["MILITARY_SCENARIO"] = [
    "Pre-Wartime", "Wartime", "Post-Wartime", "Peace time"
]

story_elements["MILITARY_PROTAGONIST"] = [
    "Junior Enlisted", "Mid-Career Enlisted", "Senior Enlisted",
    "Junior Officer", "Mid-Career Officer", "Senior Officer", "Veteran", "military affiliated civilian",
    "military affiliated contractor", "Dependent spouse", "Dependent child", "grizzled combat veteran", "retiree", "a civilian who never served",
    "Conscript", "Child soldier", "With unknown military Status", "Defector", "Consciencious Objector", "Mercenary", 
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
    "Ghost of Tsushima", "Control", "Hellblade: Senua's Sacrifice" , "Final Fantasy IV", "Final Fantasy V", "Final Fantasy VI",
    "Final Fantasy VII", "Final Fantasy VIII", "Final Fantasy IX", "Final Fantasy X", "Final Fantasy XII", "Final Fantasy XIII",
    "Final Fantasy XIII-2", "Lightning Returns: Final Fantasy XIII", "Final Fantasy Tactics"
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


# Now, all your categories are formatted and ready for use in your story generator.





def select_random_element(category):
    return random.choice(story_elements[category])

def generate_story():
    story = f"This story is about a {select_random_element('CHARACTER_DESCRIPTOR')} {select_random_element('CHARACTER_GENDER')} {select_random_element('MILITARY_PROTAGONIST')} {select_random_element('JOBS')} during {select_random_element('MILITARY_SCENARIO')}. "
    story += f"Their goal is to {select_random_element('CHARACTER_GOALS')}. \n"
    story += f"But {select_random_element('CHARACTER_DESCRIPTOR')} {select_random_element('BASIC_EVENT')} gets in their way. \n\n"
    story += f"The major event of the story involves {select_random_element('BASIC_EVENT')}. "
    story += f"This is a {select_random_element('STORY_DESCRIPTOR')} {select_random_element('STORY_TYPE')}-themed story, "
    story += f"with a {select_random_element('STORY_DESCRIPTOR')} ending. \n\n"
    story += f"The piece of technology central to the plot is the {select_random_element('TECHNOLOGY_FUNCTION')} {select_random_element('TECHNOLOGY_OBJECT')}. "
    story += f"This is known to cause {select_random_element('EMOTION_AMPLIFIER')} leading to {select_random_element('EMOTION')}. \n\n"
    story += f"It is also rumored to allow the user the ability of: {select_random_element('SUPERHUMAN_ABILITY')}.\n\n"
    story += f"Elements and themes from the video game {select_random_element('VIDEO_GAME_FRANCHISE')} are adapted in this story."

    return story

# Generate a story
print(generate_story())
