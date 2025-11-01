import cv2
import numpy as np

class KeyFrame:
    def __init__(self, duration, background):
        """
        initializes a keyframe

        :param duration: how long the keyframe will show in the animation in frames
        :type duration: int
        :param background: background image
        :type background: PIL.Image.Image
        """
        self.duration = duration
        self.image = background

    def paste(self, overlay, center, angle=0):
        """
        paste an image onto the keyframe

        :param overlay: image to be pasted
        :type overlay: PIL.Image.Image
        :param center: center coordinate
        :type center: tuple[int, int]
        :param angle: tilted angle in degrees
        :type angle: float
        """
        if angle:
            overlay = overlay.rotate(angle, expand=True)

        overlay_center = overlay.width // 2, overlay.height // 2
        top_left = center[0] - overlay_center[0], center[1] - overlay_center[1]

        self.image.paste(overlay, top_left, mask=overlay)

    def preview(self):
        """
        show a preview of the keyframe
        """
        self.image.show()

    def write(self, writer):
        """
        adds the keyframe to a video writer with appropriate duration
        you won't have to use this function normally, this is reserved
        for generator.py

        :param writer: video writer
        :type writer: cv2.VideoWriter
        :return:
        """
        cv_frame = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        for _ in range(self.duration):
            writer.write(cv_frame)

def resize(image, scale):
    """
    resize an image's width and height with respect to a given scale
    if scale is a single float both width and height get scaled equally

    :param image: image to be resized
    :type image: PIL.Image.Image
    :param scale: scaling factor
    :type scale: float | tuple[float, float]
    """
    if type(scale) == tuple:
        width_factor, height_factor = scale
    else:
        width_factor = height_factor = scale

    new_width = int(image.width * width_factor)
    new_height = int(image.height * height_factor)
    return image.resize((new_width, new_height))

def paste_center(background, overlay, center, angle=0):
    """
    paste an image onto a background, similar to KeyFrame.paste()

    :param background: background image
    :type background: PIL.Image.Image
    :param overlay: image to be pasted
    :type overlay: PIL.Image.Image
    :param center: center coordinate
    :type center: tuple[int, int]
    :param angle: tilted angle in degrees
    :type angle: float
    """
    if angle:
        overlay = overlay.rotate(angle, expand=True)

    overlay_center = overlay.width // 2, overlay.height // 2
    top_left = center[0] - overlay_center[0], center[1] - overlay_center[1]

    background.paste(overlay, top_left, mask=overlay)
