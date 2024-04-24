
from flask import Flask, render_template
from militarygame_techrandomstorygenerator import generate_world, generate_story, generate_character, generate_destiny_dice, generate_scene

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Military Game-Tech Fiction Story Generator!"

@app.route('/generate_world', methods=['GET'])
def gen_world():
    world = generate_world()
    return render_template('story.html', story=world, type='World')

@app.route('/generate_story', methods=['GET'])
def gen_story():
    story = generate_story()
    return render_template('story.html', story=story, type='Story')

@app.route('/generate_character', methods=['GET'])
def gen_character():
    character = generate_character()
    return render_template('story.html', story=character, type='Character')

@app.route('/generate_destiny_dice', methods=['GET'])
def gen_destiny_dice():
    destiny = generate_destiny_dice()
    return render_template('story.html', story=destiny, type='Destiny Dice')

@app.route('/generate_scene', methods=['GET'])
def gen_scene():
    scene = generate_scene()
    return render_template('story.html', story=scene, type='Scene')

if __name__ == '__main__':
    app.run(debug=True)







