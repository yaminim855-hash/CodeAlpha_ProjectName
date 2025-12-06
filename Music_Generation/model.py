from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def build_model(input_shape, n_vocab):
    """
    input_shape: (sequence_length, 1)
    n_vocab: number of unique notes
    """
    model = Sequential()
    model.add(LSTM(256, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(256))
    model.add(Dropout(0.3))
    model.add(Dense(256, activation="relu"))
    model.add(Dense(n_vocab, activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model
