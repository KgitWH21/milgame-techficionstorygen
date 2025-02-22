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
        
    )

story = create_story()

print(create_story())





