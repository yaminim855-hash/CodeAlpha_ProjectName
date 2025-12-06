# AI Music Generator (LSTM + MIDI)

This project generates new music using an LSTM neural network trained on MIDI files.  
The model learns note sequences and outputs a new melody in MIDI format.

---

## Features
- MIDI file preprocessing using Music21
- LSTM model (TensorFlow/Keras)
- Generates new MIDI music
- Customizable sequence length and training dataset
- Easy to extend with more MIDI data

---

## Project Structure

```
project_folder/
│── data/
│── preprocess.py
│── train.py
│── generate.py
│── model.py
│── requirements.txt
│── metadata.pkl
│── music_model.h5
│── README.md
```

---

## Technologies Used
- Python 3.x  
- TensorFlow / Keras  
- Music21  
- NumPy  
- Pickle  

---

## Installation

```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. Add MIDI Files
Place your `.mid` files inside the **data/** folder.

### 2. Preprocess the data
```bash
python preprocess.py
```

### 3. Train the model
```bash
python train.py
```

### 4. Generate music
```bash
python generate.py
```

Output file:
```
generated_music.mid
```

---

## How It Works

1. MIDI notes are extracted and saved as sequences  
2. LSTM model learns patterns between notes  
3. Model predicts new note sequences  
4. Output is converted back into a MIDI file  

---

## Core LSTM Model (Simplified)

```python
model = Sequential([
    LSTM(256, input_shape=(sequence_len, 1), return_sequences=True),
    Dropout(0.3),
    LSTM(256),
    Dense(n_vocab, activation="softmax")
])
```

---

## Future Improvements
- Add more MIDI genres (jazz, classical, pop)
- Add GAN-based music generation
- Add web interface to play the MIDI output
- Deploy using Flask/Streamlit

---

## Author
Medaballi Yamini
