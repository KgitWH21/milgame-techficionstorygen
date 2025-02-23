import json
import random

# Load story elements from JSON
with open('story_elements.json', 'r') as f:
    story_elements = json.load(f)

def select_random_element(category, subcategory):
    return random.choice(story_elements[category][subcategory])

def create_story():
    return (
        "STORY: \n\n"
        f"This story follows the plot archetype: {select_random_element('plot', 'archetypes')}. \n\n"
        f"It is written in {select_random_element('plot', 'perspectives')} perspective. \n\n"
        f"The main character is a {select_random_element('character', 'descriptors')} "
        f"{random.randint(1, 130)}-year-old "
        f"{select_random_element('character', 'race')} who is {select_random_element('character', 'gender')} "
        f"and has a relationship status of{select_random_element('character', 'relationship')}. \n\n"
    )

story = create_story()

print(create_story())





