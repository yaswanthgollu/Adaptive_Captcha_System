from flask import Flask, request, render_template, jsonify, redirect, session, send_file
from captcha_generator import generate_captcha
import os 
import time

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    captcha_text, image_path = generate_captcha(session.get('captcha_level', 'easy'))
    session['captcha_text'] = captcha_text
    session['image_path'] = image_path
    session['start_time'] = time.time()
    return render_template('index.html', captcha_image=image_path)

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('captcha_input')
    time_taken = time.time() - session['start_time']

    # Difficulty adjustment
    if time_taken < 2:
        session['captcha_level'] = 'hard'
    elif time_taken < 6:
        session['captcha_level'] = 'medium'
    else:
        session['captcha_level'] = 'easy'

    if user_input == session['captcha_text']:
        return render_template('result.html', result="Success!", time=round(time_taken, 2))
    else:
        return render_template('result.html', result="Failed!", time=round(time_taken, 2))
    
@app.route('/captcha/<filename>')
def serve_captcha(filename):
    return send_file(os.path.join('static', 'captchas', filename), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)