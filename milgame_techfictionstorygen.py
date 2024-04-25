
from flask import Flask, render_template, send_from_directory
from militarygame_techrandomstorygenerator import create_world, create_story, create_character, create_destiny_dice, create_scene

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Military Game-Tech Fiction Story Generator!"

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


@app.route('/generate_world', methods=['GET'])
def gen_world():
    world = create_world()
    return render_template('story.html', story=world, type='World')

@app.route('/generate_story', methods=['GET'])
def gen_story():
    story = create_story()
    return render_template('story.html', story=story, type='Story')

@app.route('/generate_character', methods=['GET'])
def gen_character():
    character = create_character()
    return render_template('story.html', story=character, type='Character')

@app.route('/generate_destiny_dice', methods=['GET'])
def gen_destiny_dice():
    destiny = create_destiny_dice()
    return render_template('story.html', story=destiny, type='Destiny Dice')

@app.route('/generate_scene', methods=['GET'])
def gen_scene():
    scene = create_scene()
    return render_template('story.html', story=scene, type='Scene')

if __name__ == '__main__':
    app.run(debug=True)







