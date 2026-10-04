import numpy as np
from ai.gesture_recognition import detect_gesture


def test_empty_depth_is_none():
    result = detect_gesture(np.zeros((10, 10), dtype=np.uint16))
    assert result.name == "none"


def test_near_region_detects_hand():
    depth = np.full((100, 100), 2000, dtype=np.uint16)
    depth[40:60, 40:60] = 500
    result = detect_gesture(depth, threshold_mm=900, min_pixels=100)
    assert result.name == "hand_detected"
    assert result.center == (49, 49)
