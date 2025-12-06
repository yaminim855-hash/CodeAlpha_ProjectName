import pickle
import numpy as np
from keras.models import load_model
from music21 import instrument, note, chord, stream
import random


def generate_notes(model, metadata, num_generate=200):
    note_to_int = metadata["note_to_int"]
    int_to_note = metadata["int_to_note"]
    sequence_length = metadata["sequence_length"]
    n_vocab = metadata["n_vocab"]

    # for generation we need integer input sequences
    # simple seed: random sequence of existing note indices
    pattern = [note_to_int[n] for n in list(note_to_int.keys())[:sequence_length]]
    pattern = pattern[:sequence_length]

    output_notes = []

    for _ in range(num_generate):
        # reshape to (1, sequence_length, 1) and normalize
        input_seq = np.reshape(pattern, (1, sequence_length, 1))
        input_seq = input_seq / float(n_vocab)

        prediction = model.predict(input_seq, verbose=0)[0]
        index = int(np.argmax(prediction))
        predicted_note = int_to_note[index]

        output_notes.append(predicted_note)

        # slide window
        pattern.append(index)
        pattern = pattern[1:]

    return output_notes


def create_midi(prediction_output, output_file="generated_music.mid"):
    offset = 0
    output_notes = []

    for pattern in prediction_output:
        # chord
        if "." in pattern or pattern.isdigit():
            notes_in_chord = pattern.split(".")
            chord_notes = []
            for n in notes_in_chord:
                new_note = note.Note(int(n))
                new_note.storedInstrument = instrument.Piano()
                chord_notes.append(new_note)
            new_chord = chord.Chord(chord_notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            # single note
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        offset += 0.5  # step

    midi_stream = stream.Stream(output_notes)
    midi_stream.write("midi", fp=output_file)
    print("MIDI file generated:", output_file)


if __name__ == "__main__":
    # load model and metadata
    model = load_model("music_model.h5")
    with open("metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    prediction_output = generate_notes(model, metadata, num_generate=200)
    create_midi(prediction_output, "generated_music.mid")
