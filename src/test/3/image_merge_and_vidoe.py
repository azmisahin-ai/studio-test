import cv2
import os

def images_to_video(image_folder, video_name, fps=1):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

# Kullanım örneği
images_folder = 'assets'
video_name = 'output.mp4'
fps = 1  # Saniyede kaç kare

images_to_video(images_folder, video_name, fps)
