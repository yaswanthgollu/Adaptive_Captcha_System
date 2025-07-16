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

    def get_difficulty_level(time_taken):
        if time_taken < 2:
            return 5  # Very Hard
        elif time_taken < 4:
            return 4
        elif time_taken < 6:
            return 3
        elif time_taken < 8:
            return 2
        else:
            return 1  

    if user_input == session['captcha_text']:
        session['captcha_level'] = get_difficulty_level(time_taken)
        return render_template('result.html', result="Success!", time=round(time_taken, 2))
    else:
        return render_template('result.html', result="Failed!", time=round(time_taken, 2))
    
@app.route('/captcha/<filename>')
def serve_captcha(filename):
    return send_file(os.path.join('static', 'captchas', filename), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)