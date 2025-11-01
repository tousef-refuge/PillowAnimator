#the file name MUST be frames.py, and any variables must be named as they are

from helpers import *
from PIL import Image
from pathlib import Path

##initializations
#images
BASE_DIR = Path(__file__).resolve().parent
bg = Image.open(BASE_DIR / "imgs" / "big_bg.png")
ball = Image.open(BASE_DIR / "imgs" / "ball.png")
ball = resize(ball, 0.3)

#configuration
width, height = bg.size
fps = 24

#actual frames
frames = []

"im not showing them its a mess lmao"

#keyframe 1
f1 = KeyFrame(2, bg.copy())
f1.paste(ball, (600, 100))
frames.append(f1)

#keyframe 2
f2 = KeyFrame(2, bg.copy())
f2.paste(ball, (600, 120))
frames.append(f2)

#keyframe 3
f3 = KeyFrame(2, bg.copy())
ball1 = ball.copy()
ball1 = resize(ball1, (0.95, 1.05))
f3.paste(ball, (600, 150))
frames.append(f3)

#keyframe 4
f4 = KeyFrame(2, bg.copy())
ball2 = ball.copy()
ball2 = resize(ball2, (0.9, 1.1))
f4.paste(ball2, (600, 190))
frames.append(f4)

#keyframe 5
f5 = KeyFrame(2, bg.copy())
ball3 = ball.copy()
ball3 = resize(ball3, (0.7, 1.3))
f5.paste(ball3, (600, 250))
frames.append(f5)

#keyframe 6
f6 = KeyFrame(1, bg.copy())
ball4 = ball.copy()
ball4 = resize(ball4, (0.6, 1.4))
f6.paste(ball4, (600, 400))
frames.append(f6)

#keyframe 7
f7 = KeyFrame(1, bg.copy())
f7.paste(ball2, (600, 650))
frames.append(f7)

frames2 = frames[::-1]

#keyframe 8 idk
f8 = KeyFrame(2, bg.copy())
ball6 = ball.copy()
ball6 = resize(ball6, (1.5, 0.5))
f8.paste(ball6, (600, 700))
frames.append(f8)

frames.extend(frames2)
frames.pop()

#the last
f9 = KeyFrame(1, bg.copy())
f9.paste(ball, (600, 99))
frames.append(f9)