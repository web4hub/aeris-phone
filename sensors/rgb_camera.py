from __future__ import annotations
from typing import Optional
import cv2


class RGBCamera:
    def __init__(self, device_index: int = 0, width: int = 640, height: int = 480):
        self.cap = cv2.VideoCapture(device_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    @property
    def opened(self) -> bool:
        return bool(self.cap.isOpened())

    def get_frame(self) -> Optional[object]:
        ok, frame = self.cap.read()
        return frame if ok else None

    def release(self) -> None:
        self.cap.release()
