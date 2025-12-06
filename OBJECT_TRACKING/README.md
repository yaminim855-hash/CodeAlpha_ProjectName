# Object Detection and Tracking (YOLO + Tracker)

This project performs real-time object detection and tracking using YOLO and built-in SORT/ByteTrack trackers.  
It supports webcam input and video files.

---

## Features
- Real-time object detection using YOLO models
- Multi-object tracking with unique IDs
- Works with webcam or video
- Detects 80+ COCO classes
- High accuracy + smooth tracking

---

## Project Structure

```
project_folder/
│── main.py
│── tracker.py
│── requirements.txt
│── README.md
```

---

## Technologies Used
- Python  
- Ultralytics YOLO  
- OpenCV  
- ByteTrack / BoT-SORT  

---

## Installation

```bash
pip install -r requirements.txt
```

---

## How to Run

### Webcam
```bash
python main.py
```

### Video File
Edit in `main.py`:

```python
source = "video.mp4"
```

---

## How It Works
1. YOLO detects objects per frame  
2. Tracker assigns a unique ID to each object  
3. Boxes, labels, and IDs are drawn on screen  
4. Video continues updating in real-time  

---

## Code Overview

```python
model = YOLO("yolo11s.pt")
model.track(source=0, show=True, tracker="bytetrack.yaml")
```

---

## Supported Objects
Detects 80+ categories such as:

- Person  
- Cell Phone  
- Car / Bike  
- Dog / Cat  
- Chair / Bottle  
- More from COCO dataset  

---

## Future Improvements
- Add counting lines (entry/exit counting)
- Add region-based tracking (ROI)
- Add alert system for selected objects
- Deploy using Streamlit/Flask

---

## Author
Medablli Yamini
