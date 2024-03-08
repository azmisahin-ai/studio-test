from moviepy.editor import VideoFileClip, AudioFileClip
from midi2audio import FluidSynth

def add_audio_and_midi_to_video(video_path, midi_path, output_path):
    # Video dosyasını yükle
    video_clip = VideoFileClip(video_path)

    # FluidSynth nesnesi oluştur
    fs = FluidSynth()

    # MIDI dosyasını çal ve sesi al
    fs.midi_to_audio(midi_path, "output.wav")

    # Ses dosyasını yükle
    audio_clip = AudioFileClip("output.wav")

    # Ses dosyasını video süresine göre kırp
    audio_clip = audio_clip.subclip(0, video_clip.duration)

    # Ses ve videoyu birleştir
    video_clip = video_clip.set_audio(audio_clip)

    # Birleştirilmiş videoyu kaydet
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Kullanım örneği
video_path = "output.mp4"
midi_path = "output.mid"
output_path = "output_with_audio_and_midi.mp4"

add_audio_and_midi_to_video(video_path, midi_path, output_path)
