from __future__ import annotations
import cv2
import numpy as np


def render_to_projector(mesh, projector_resolution=(1280, 720), point_size=2):
    """Project a mesh as a calibrated preview frame.

    This is intentionally a safe 2-D preview. It does not claim to generate
    a physical light field or diffraction hologram.
    """
    width, height = projector_resolution
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    if mesh is None or not hasattr(mesh, "vertices"):
        return frame
    vertices = np.asarray(mesh.vertices)
    if vertices.size == 0:
        return frame
    xy = vertices[:, :2].copy()
    span = np.ptp(xy, axis=0)
    span[span < 1e-6] = 1.0
    xy[:, 0] = (xy[:, 0] - xy[:, 0].min()) / span[0] * (width - 1)
    xy[:, 1] = (1.0 - (xy[:, 1] - xy[:, 1].min()) / span[1]) * (height - 1)
    for x, y in xy.astype(np.int32):
        cv2.circle(frame, (int(x), int(y)), point_size, (0, 220, 255), -1)
    return frame
