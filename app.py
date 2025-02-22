from flask import Flask, render_template
from militarygame_techrandomstorygenerator import create_story

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('story.html')

@app.route('/generate')
def generate():
    return create_story()

if __name__ == '__main__':
    app.run(debug=True) 