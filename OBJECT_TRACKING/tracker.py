# tracker.py
import math


class Track:
    def __init__(self, track_id, bbox, cls, conf):
        self.id = track_id          # tracking ID
        self.bbox = bbox            # [x1, y1, x2, y2]
        self.cls = cls              # class id
        self.conf = conf            # confidence
        self.missed = 0             # how many frames not matched


class SimpleTracker:
    """
    Very simple SORT-like tracker.
    Matches detections to existing tracks using IoU.
    """

    def __init__(self, iou_threshold=0.45, max_age=15):
        self.tracks = []
        self.next_id = 1
        self.iou_threshold = iou_threshold
        self.max_age = max_age

    @staticmethod
    def iou(b1, b2):
        x1 = max(b1[0], b2[0])
        y1 = max(b1[1], b2[1])
        x2 = min(b1[2], b2[2])
        y2 = min(b1[3], b2[3])

        inter_w = max(0, x2 - x1)
        inter_h = max(0, y2 - y1)
        inter = inter_w * inter_h

        area1 = (b1[2] - b1[0]) * (b1[3] - b1[1])
        area2 = (b2[2] - b2[0]) * (b2[3] - b2[1])

        union = area1 + area2 - inter + 1e-6
        return inter / union

    def update(self, detections):
        """
        detections = [
          {"bbox":[x1,y1,x2,y2], "cls":int, "conf":float},
          ...
        ]
        returns list[Track]
        """
        # age all tracks
        for t in self.tracks:
            t.missed += 1

        # match detections
        for det in detections:
            best_iou = 0.0
            best_track = None

            for t in self.tracks:
                iou_val = self.iou(det["bbox"], t.bbox)
                if iou_val > best_iou:
                    best_iou = iou_val
                    best_track = t

            if best_iou > self.iou_threshold and best_track is not None:
                best_track.bbox = det["bbox"]
                best_track.cls = det["cls"]
                best_track.conf = det["conf"]
                best_track.missed = 0
            else:
                # new track
                new_track = Track(
                    track_id=self.next_id,
                    bbox=det["bbox"],
                    cls=det["cls"],
                    conf=det["conf"],
                )
                self.tracks.append(new_track)
                self.next_id += 1

        # remove lost tracks
        self.tracks = [t for t in self.tracks if t.missed <= self.max_age]
        return self.tracks
