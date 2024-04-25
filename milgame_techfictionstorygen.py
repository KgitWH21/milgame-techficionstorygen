
from flask import Flask, render_template, send_from_directory
from militarygame_techrandomstorygenerator import create_world, create_story, create_character, create_destiny_dice, create_scene, world, scene, story, character, destiny_dice

app = Flask(__name__)

@app.route('/')
def home():
    world = create_world()  # Move this line here
    return render_template('story.html', world=world, story=story, scene=scene, character=character, destiny_dice=destiny_dice) 

def generate_world() -> str:
    # Your logic to create the world (should return a string)
    world = "..."
    return world

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


@app.route('/generate_world', methods=['GET'])
def generate_world():
    new_world = create_world()  # Call your world generation function
    return new_world  # Return the raw text content

@app.route('/generate_story', methods=['GET'])  # Removed 'methods=['GET']' 
def generate_story():
    new_story = create_story()
    return new_story  # Return raw text, not rendering

@app.route('/generate_character', methods=['GET'])  # Removed 'methods=['GET']' 
def generate_character():
    new_character = create_character()
    return new_character  # Return raw text, not rendering

@app.route('/generate_destiny_dice', methods=['GET'])
def gen_destiny_dice():
    destiny = create_destiny_dice()
    return destiny

@app.route('/generate_scene', methods=['GET'])
def gen_scene():
    scene = create_scene()
    return scene



if __name__ == '__main__':
    app.run(debug=True)

print(world)






