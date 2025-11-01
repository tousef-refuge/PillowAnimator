------------------BORING INTRODUCTION------------------

PillowAnimator is a project I made because I was bored
Juggling time between programming and drawing is SOOOOO tiring...if
only there was a handsome genius out there who combined both

How PillowAnimator works is that it uses python's Pillow package along
with some other tech to combine Images and make an animation

It's like OpenToonz but way worse to use, like unless you're a
programmer I think this project genuinely offers no tactical advantage
over just using a regular animation software lmao, but what does matter
is you can flex to others that your medium of choice is Pycharm so
obviously PillowAnimator reigns supreme

Anyways despite how it looks it's not actually that hard to operate.
The only somewhat inconvenient thing is actually making the frames but
in a way that has its advantages too since you can adjust images with
precision down to the pixel

Here's how you can make your VERY OWN!!! PillowAnimator project

---------------SETTING UP THE DIRECTORIES---------------

Before you start actually writing code you need to set up your project's
directory. All projects go in the project directory that's given.
Make a new directory for your project. We'll call it tutorial for now

Once that's set up, in the templates directory there's a file called
frames.py, which you can copy into your project. This file is ESSENTIAL
to actually generating the animation. There's instructions on how it works
in the file and how to write stuff in it

Optionally, you can add another directory imgs. This is where you put your
images to paste into your frames. In the template file frames.py it uses
two images bg.png and ball.png so we'll consider these in this tutorial.
The imgs directory isn't absolutely necessary but it helps a lot with
organization

Pillow Animator also has the option to use audio, so if you want to you
can put a wav, mp3 OR ogg file to your project. If there's multiple
valid audio files the generator file prioritizes wav -> mp3 -> ogg
but we'll talk about the generator file a bit more in depth later.
The audio file itself though MUST be called audio.xx, otherwise the
generator ignores it and won't add it to your video

If everything is done right it should look like this:
```
└── projects
     └── tutorial
          ├── imgs
          │   └── ball.png
          │   └── bg.png
          └── audio.xx
          └── frames.py
```
Once that's done you can move on to actually generating the video

----------------GENERATING THE ANIMATION----------------

The generator.py file is responsible for actually making the animation.
The only thing you need to do here is adjust a couple paramters under
initial configurations. Running the file does the rest of the magic.

directory = directory of your project. Preferably you start it with
            projects/ but the program autocorrects it
add_audio = decides whether to add audio to the mp4 or not
make_gif  = decides whether to generate the gif. Turn this off for
            bigger animations since it saves a lot of time
preview   = decides whether to preview your animation or not.
            keep in mind when audio is added, the program
            will preview the mp4 instead of the gif
            if the gif isn't made the mp4 gets reviewed instead

Once that's done just run the program and it should be done in a
couple of seconds (unless you're recreating an entire jojo op from
scratch but nobody's gonna do that right? haha hahaha)

The final animation should be found in your project directory in a
new directory called output. It contains an mp4 and a gif if make_gif
was set to True
```
└── projects
     └── tutorial
          ├── imgs
          │   └── ball.png
          │   └── bg.png
          ├── output
          │   └── output.gif
          │   └── output.mp4
          └── audio.xx
          └── frames.py
```

Congratulations! You made your first animation! Now think about all
the time you wasted actually making it and look back at it and realize
that using flipaclip or something was way more efficient