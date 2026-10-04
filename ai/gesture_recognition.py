from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple
import numpy as np


@dataclass(frozen=True)
class Gesture:
    name: str
    center: Optional[Tuple[int, int]] = None
    confidence: float = 0.0


def detect_gesture(depth_image, threshold_mm=900, min_pixels=300) -> Gesture:
    depth = np.asarray(depth_image)
    if depth.ndim != 2 or depth.size == 0:
        return Gesture("none")
    mask = (depth > 0) & (depth < threshold_mm)
    count = int(mask.sum())
    if count < min_pixels:
        return Gesture("none")
    ys, xs = np.nonzero(mask)
    center = (int(xs.mean()), int(ys.mean()))
    confidence = min(1.0, count / max(min_pixels * 4, 1))
    return Gesture("hand_detected", center, confidence)


def detect_gestures(depth_image, threshold=50):
    # Backward-compatible API from the original prototype.
    return detect_gesture(depth_image, threshold_mm=threshold).name
