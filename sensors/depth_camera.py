from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple
import numpy as np

try:
    import pyrealsense2 as rs
except ImportError:
    rs = None


@dataclass
class DepthFrame:
    depth: np.ndarray
    color: np.ndarray


class DepthCamera:
    """Intel RealSense RGB-D adapter with an explicit lifecycle."""

    def __init__(self, width: int = 640, height: int = 480, fps: int = 30):
        if rs is None:
            raise RuntimeError("pyrealsense2 is not installed")
        self.width, self.height, self.fps = width, height, fps
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
        self.config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
        self.profile = None

    def start(self) -> None:
        if self.profile is None:
            self.profile = self.pipeline.start(self.config)

    def get_frames(self) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        if self.profile is None:
            self.start()
        frames = self.pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        color = frames.get_color_frame()
        if not depth or not color:
            return None, None
        return np.asanyarray(depth.get_data()), np.asanyarray(color.get_data())

    def stop(self) -> None:
        if self.profile is not None:
            self.pipeline.stop()
            self.profile = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *_):
        self.stop()
