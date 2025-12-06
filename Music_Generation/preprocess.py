from music21 import converter, instrument, note, chord
import glob
import pickle
import os

def extract_notes(midi_folder="data"):
    notes = []

    if not os.path.exists(midi_folder):
        print(f"Folder '{midi_folder}' not found.")
        return notes

    files = glob.glob(os.path.join(midi_folder, "*.mid"))
    if not files:
        print("No .mid files found in 'data/' folder.")
        return notes

    for file in files:
        print("Parsing:", file)
        try:
            midi = converter.parse(file)
        except Exception as e:
            print(f"Error parsing {file}: {e}")
            continue

        parts = instrument.partitionByInstrument(midi)
        if parts:  # file with multiple instruments
            elements_to_parse = parts.parts[0].recurse()
        else:
            elements_to_parse = midi.flat.notes

        for element in elements_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                # represent chord as dot-separated string of notes
                notes.append('.'.join(str(n) for n in element.normalOrder))

    return notes

if __name__ == "__main__":
    notes = extract_notes("data")
    print("Total notes found:", len(notes))

    if notes:
        with open("notes.pkl", "wb") as f:
            pickle.dump(notes, f)
        print("Saved notes to notes.pkl")
    else:
        print("No notes extracted. Make sure you have valid MIDI files in 'data/'.")
