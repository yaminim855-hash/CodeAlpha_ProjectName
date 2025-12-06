from ultralytics import YOLO


def main():
    """
    SK 4: Object Detection + Tracking

    - Real-time video from webcam or file
    - YOLO11s pre-trained model for object detection (80+ COCO classes)
    - Built-in multi-object tracker (BoT-SORT / ByteTrack)
    - Draws bounding boxes + labels + tracking IDs
    """

    # 🔥 Model selection:
    # "yolo11s.pt"  -> good accuracy + ok speed
    # "yolo11n.pt"  -> faster on slow PCs (less accurate)
    model_name = "yolo11n.pt"
    print(f"[INFO] Loading model: {model_name}")
    model = YOLO(model_name)  # downloads once automatically

    # 🎥 Source selection:
    # 0           -> default webcam
    # "video.mp4" -> video file path
    source = 0   # change to "your_video.mp4" for file

    print("[INFO] Starting tracking. Press 'q' window lo press chesthe close avthundi.")

    # 🚀 TRACK MODE (Ultralytics built-in):
    # - Detects objects frame by frame
    # - Assigns unique tracking IDs
    # - Draws boxes, labels, IDs for you
    results = model.track(
        source=source,
        show=True,              # OpenCV window display
        tracker="bytetrack.yaml",  # SORT-style tracker (very stable)
        conf=0.5,               # min confidence (0.5 = 50%)
        iou=0.6,                # NMS IOU threshold
        imgsz=480,              # image size (640x640). If lag: use 480
        verbose=False,
    )

    print("[INFO] Tracking finished / stopped.")


if __name__ == "__main__":
    main()

