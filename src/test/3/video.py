from moviepy.editor import ImageSequenceClip
import os
import glob


def images_to_video(image_folder, video_name, fps=1):
    images = glob.glob(os.path.join(image_folder, "*.png"))
    #images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    clip = ImageSequenceClip(images, fps=fps)
    clip.write_videofile(video_name)

# Kullanım örneği
images_folder = 'assets'
video_name = 'output.mp4'
fps = 1 # Saniyede kaç kare

images_to_video(images_folder, video_name, fps)
