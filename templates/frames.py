#the file name MUST be frames.py, and any variables must be named as they are

from helpers import *
from PIL import Image
from pathlib import Path

##initializations
#images
BASE_DIR = Path(__file__).resolve().parent
"your images go here"

#example
bg = Image.open(BASE_DIR / "imgs" / "bg.png")
ball = Image.open(BASE_DIR / "imgs" / "ball.png")

#configuration
width, height = 400, 400
fps = 24

#actual frames
frames = []

"adjust all your frames next"

#example
f1 = KeyFrame(2, bg.copy())
f1.paste(ball, (200, 200))
frames.append(f1)

f2 = KeyFrame(3, bg.copy())
rball = ball.copy()
rball = resize(rball, 0.5)
f2.paste(rball, (300, 300))
frames.append(f2)

"""
you can do KeyFrame.preview() to see how a frame looks
the KeyFrame background argument MUST be an Image.copy()
as for resizing it's preferred to resize an image the
way it's shown here if you plan to reuse an image

For more info about how these functions work check out helpers.py
"""