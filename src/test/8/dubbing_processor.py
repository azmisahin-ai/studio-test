from gtts import gTTS

# dubbing_processor.py
def process_dubbing(textArray):
  
  response_data = []  # Boş bir liste oluştur

  # Her bir öğe için döngü, hem değeri hem de indisi alınır
  for index, text in enumerate(textArray):
    file =  f"static/{index}.mp3" 
    tts = gTTS(text=text, lang="en")
    tts.save(file)
    response_data.append({
          "file": file,
          "text": text,
          })
    
  return response_data