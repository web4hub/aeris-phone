from __future__ import annotations
import cv2


def add_touch_effects(frame, hand_positions, radius=14):
    for pos in hand_positions:
        cv2.circle(frame, tuple(map(int, pos)), radius, (0, 255, 0), -1)
    return frame
