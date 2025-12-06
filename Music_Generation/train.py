import pickle
import numpy as np
from keras.utils import to_categorical   # TensorFlow 2.20+ installs keras
from model import build_model

DEFAULT_SEQUENCE_LENGTH = 8   # small dataset kabatti


def prepare_sequences(notes, sequence_length: int):
    """Convert list of notes -> input/output sequences for training."""
    # unique notes
    pitches = sorted(set(notes))
    n_vocab = len(pitches)

    note_to_int = {note: number for number, note in enumerate(pitches)}
    int_to_note = {number: note for note, number in note_to_int.items()}

    network_input = []
    network_output = []

    # sequences create chey
    for i in range(0, len(notes) - sequence_length):
        seq_in = notes[i:i + sequence_length]
        seq_out = notes[i + sequence_length]
        network_input.append([note_to_int[note] for note in seq_in])
        network_output.append(note_to_int[seq_out])

    n_patterns = len(network_input)
    print("Number of sequences (patterns):", n_patterns)

    if n_patterns == 0:
        raise ValueError(
            f"Not enough notes to create even 1 pattern. "
            f"Total notes = {len(notes)}, sequence_length = {sequence_length}"
        )

    # reshape & normalize
    network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
    network_input = network_input / float(n_vocab)

    network_output = to_categorical(network_output)

    return network_input, network_output, note_to_int, int_to_note, n_vocab


if __name__ == "__main__":
    # load notes from preprocessing
    with open("notes.pkl", "rb") as f:
        notes = pickle.load(f)

    print("Total notes:", len(notes))

    # dataset size batti sequence length automatic ga set chestunnam
    # ex: 13 notes unte -> min(8, 12) = 8
    sequence_length = min(DEFAULT_SEQUENCE_LENGTH, max(2, len(notes) - 1))
    print(f"Using sequence length: {sequence_length}")

    network_input, network_output, note_to_int, int_to_note, n_vocab = prepare_sequences(
        notes, sequence_length
    )

    # build model
    model = build_model(
        input_shape=(network_input.shape[1], network_input.shape[2]),
        n_vocab=n_vocab
    )

    # train
    model.fit(network_input, network_output, epochs=20, batch_size=64)
    model.save("music_model.h5")
    print("Model saved as music_model.h5")

    # save metadata for generation
    metadata = {
        "note_to_int": note_to_int,
        "int_to_note": int_to_note,
        "sequence_length": sequence_length,
        "n_vocab": n_vocab,
    }

    with open("metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("Metadata saved to metadata.pkl")
