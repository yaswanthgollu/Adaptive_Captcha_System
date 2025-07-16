from captcha.image import ImageCaptcha
import random
import string
import os
import time

def generate_captcha(level=1):
    levels = {
        1: (string.ascii_lowercase, 4),
        2: (string.ascii_lowercase + string.digits, 5),
        3: (string.ascii_letters + string.digits, 6),
        4: (string.ascii_letters + string.digits + "!@#", 7),
        5: (string.ascii_letters + string.digits + "!@#$%^&*", 8)
    }

    chars, length = levels.get(level, levels[1])
    text = ''.join(random.choices(chars, k=length))

    os.makedirs("static/captchas", exist_ok=True)
    image = ImageCaptcha(width=250, height=90, font_sizes=[48])
    
    import time
    unique_id = str(int(time.time() * 1000))
    filename = f"{text}_{unique_id}.png"
    file_path = f"static/captchas/{filename}"
    
    image.write(text, file_path)
    return text, f"captcha/{filename}"
