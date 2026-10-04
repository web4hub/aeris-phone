from __future__ import annotations
import cv2


def encode_jpeg(frame, quality=85):
    ok, encoded = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, int(quality)])
    if not ok:
        raise ValueError("Could not encode frame")
    return encoded.tobytes()
