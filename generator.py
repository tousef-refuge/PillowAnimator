import os
import cv2
import importlib.util
import webbrowser
import sys
import time

from moviepy import VideoFileClip, AudioFileClip
from contextlib import contextmanager

#initial configurations
directory = "projects/test_project"
add_audio = False
make_gif = True
preview = True

def main():
    global directory
    global add_audio
    start = time.time()

    #extract directory and variables
    if not directory.startswith("projects/"):
        directory = f"projects/{directory}"

    output_dir = os.path.join(directory, "output")
    os.makedirs(output_dir, exist_ok=True)

    frames_path = os.path.join(directory, "frames.py")
    if not os.path.isfile(frames_path):
        raise FileNotFoundError(f"No frames.py found in {directory}")

    spec = importlib.util.spec_from_file_location("frames", frames_path)
    frames_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(frames_module)

    frames = frames_module.frames
    width = frames_module.width
    height = frames_module.height
    fps = frames_module.fps

    #video writer
    video_path = os.path.join(output_dir, "output.mp4")
    out = cv2.VideoWriter(
        video_path,
        cv2.VideoWriter_fourcc(*"mp4v"), #type: ignore[attr-defined]
        fps,
        (width, height)
    )
    for frame in frames:
        frame.write(out)

    out.release()
    print(f"Video saved as {video_path}")

    #audio writer
    audio_path = None
    for ext in "wav", "mp3", "ogg":
        candidate = os.path.join(directory, f"audio.{ext}")
        if os.path.isfile(candidate):
            audio_path = candidate
            break

    if audio_path and add_audio:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        if audio_clip.duration > video_clip.duration:
            audio_clip = audio_clip.subclipped(0, video_clip.duration)

        final_clip = video_clip.with_audio(audio_clip)
        with suppress():
            final_clip.write_videofile(
                video_path,
                codec="libx264",
                audio_codec="aac",
            )

        print(f"Audio added to {video_path}")
    else:
        print(f"{'File audio.xx not found' if add_audio else 'Audio embedding denied'}. Skipping audio")
        add_audio = False

    #gif writer and preview
    gif_path = None
    if make_gif:
        images = [keyframe.image.copy() for keyframe in frames]
        durations = [int(1000 / fps * keyframe.duration) for keyframe in frames]

        gif_path = os.path.join(output_dir, "output.gif")
        images[0].save(
            gif_path,
            save_all=True,
            append_images=images[1:],
            duration=durations,
            loop=0,
            disposal=2
        )
        print(f"Gif saved as {gif_path}")

    if preview:
        webbrowser.open(video_path if (add_audio or not make_gif) else gif_path)

    print(f"\nFinished in {time.time() - start:.3f} seconds")

@contextmanager
def suppress():
    """
    makes moviepy shut the fuck up
    """
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

if __name__ == "__main__":
    main()
