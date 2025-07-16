from captcha.image import ImageCaptcha
import random
import string
import os
import time

def generate_captcha(difficulty='easy'):
    characters = {
        'easy': string.ascii_lowercase,
        'medium': string.ascii_letters + string.digits,
        'hard': string.ascii_letters + string.digits + "@#&$"
    }

    length = {'easy': 4, 'medium': 6, 'hard': 8}[difficulty]
    text = ''.join(random.choices(characters[difficulty], k=length))

    # Ensure directory exists
    os.makedirs("static/captchas", exist_ok=True)

    unique_id = str(int(time.time() * 1000))
    filename = f"{text}_{unique_id}.png"
    file_path = f"static/captchas/{filename}"

    image = ImageCaptcha(width=250, height=90, font_sizes=[48])
    image.write(text, file_path)

    return text, f"captcha/{filename}"
