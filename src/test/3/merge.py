from moviepy.editor import VideoFileClip, AudioFileClip

def add_audio_to_video(video_path, audio_path, output_path):
    """
    Ses dosyasını video dosyasına ekler.

    Parametreler:
        video_path (str): Video dosyasının yolu.
        audio_path (str): Ses dosyasının yolu.
        output_path (str): Birleştirilmiş video dosyasının kaydedileceği yol.

    Döndürülen Değer:
        None
    """

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Ses dosyasını video süresine göre kırp
    audio_clip = audio_clip.subclip(0, video_clip.duration)

    # Ses ve videoyu birleştir
    video_clip = video_clip.set_audio(audio_clip)

    # Birleştirilmiş videoyu kaydet
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Kullanım örneği
video_path = "output.mp4"
audio_path = "dubbing.mp3"
output_path = "output_with_dubbing.mp4"

add_audio_to_video(video_path, audio_path, output_path)
