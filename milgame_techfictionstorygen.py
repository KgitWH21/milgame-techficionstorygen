from flask import Flask, render_template

from militarygame_techrandomstorygenerator import generate_story


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Military Game-Tech Fiction Story Generator!"

@app.route('/generate', methods=['GET'])
def generate():
    story = generate_story()  # Make sure this function is defined
    return render_template('story.html', story=story)  # Ensure 'story.html' exists in a 'templates' folder


if __name__ == '__main__':
    app.run(debug=True)






