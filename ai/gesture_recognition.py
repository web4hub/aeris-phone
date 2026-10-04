import numpy as np

def detect_gestures(depth_image, threshold=50):
    hand_mask = depth_image < threshold
    if np.sum(hand_mask) > 1000:
        return "hand_detected"
