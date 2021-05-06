from conf import INPUTS, OUTPUTS
import os
import random
from moviepy.editor import *
from PIL import Image

video_path = os.path.join(INPUTS, 'wakeup.mp4')
thumbnails = os.path.join(OUTPUTS, 'thumbnails')
names = "abcdefghijkrmnop"

video = VideoFileClip(video_path)

fbs = video.reader.fps
nframes = video.reader.nframes
duration = video.duration
max_duration = int(duration) + 1
#frame_at_second = 6
#frame = video.get_frame(frame_at_second)
#new_image_filepath = os.path.join(thumbnails,f"{frame_at_second}.jpg")
#new_image = Image.fromarray(frame)
#new_image.save(new_image_filepath)

for i in range(0, 15):
    frame = video.get_frame(i)
    random_image_name = random.sample(names, 7)
    new_image_filepath = os.path.join(thumbnails,f"{random_image_name}.jpg")
    new_image = Image.fromarray(frame)
    new_image.save(new_image_filepath)

