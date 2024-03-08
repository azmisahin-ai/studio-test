from midiutil import MIDIFile

def create_midi_file(output_file):
    # MIDI dosyası oluşturma
    midi = MIDIFile(1)
    midi.addTempo(0, 0, 120)

    # Metin tabanlı notaları ekleyerek müzik oluşturma
    notes = [
        {"pitch": 60, "duration": 1},  # Do 1 tick
        {"pitch": 62, "duration": 2},  # Re 2 tick
        {"pitch": 64, "duration": 4},  # Mi 4 tick
        {"pitch": 65, "duration": 8},  # Fa 8 tick
    ]

    current_time = 0
    for note in notes:
        midi.addNote(0, 0, note["pitch"], current_time, note["duration"], 100)
        current_time += note["duration"]

    # MIDI dosyasını kaydetme
    with open(output_file, "wb") as midi_file:
        midi.writeFile(midi_file)

# Kullanım örneği
create_midi_file("output.mid")
