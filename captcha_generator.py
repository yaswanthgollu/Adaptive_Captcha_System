from captcha.image import ImageCaptcha
import random
import string
import os

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

    image = ImageCaptcha()
    file_path = f"static/captchas/{text}.png"
    image.write(text, file_path)

    return text, f"captcha/{text}.png"
