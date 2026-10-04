from __future__ import annotations

import argparse
import time
import numpy as np
import cv2

from aeris.config import load_config
from aeris.pipeline import AERISPipeline
from sensors.depth_camera import DepthCamera


def synthetic_frame(width=640, height=480):
    depth = np.full((height, width), 1800, dtype=np.uint16)
    color = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.rectangle(color, (120, 100), (520, 380), (70, 70, 70), -1)
    cv2.circle(depth, (width // 2, height // 2), 80, 500, -1)
    return depth, color


def parse_args():
    p = argparse.ArgumentParser(description="AERIS spatial phone runtime")
    p.add_argument("--config", default="config/config.yaml")
    p.add_argument("--camera", choices=["auto", "realsense", "simulate"], default="auto")
    p.add_argument("--headless", action="store_true")
    p.add_argument("--frames", type=int, default=0, help="0 means run until quit")
    return p.parse_args()


def main():
    args = parse_args()
    cfg = load_config(args.config)
    mode = args.camera
    if mode == "auto":
        mode = cfg.camera.get("mode", "auto")
        if mode == "auto":
            mode = "realsense"

    pipeline = AERISPipeline(cfg)
    camera = None

    if mode == "realsense":
        try:
            camera = DepthCamera(
                int(cfg.camera["width"]),
                int(cfg.camera["height"]),
                int(cfg.camera["fps"]),
            )
            camera.start()
        except Exception as exc:
            print(f"[AERIS] RealSense unavailable: {exc}")
            print("[AERIS] Falling back to simulation.")
            mode = "simulate"

    count = 0
    try:
        while args.frames == 0 or count < args.frames:
            if mode == "simulate":
                depth, color = synthetic_frame(
                    int(cfg.camera["width"]), int(cfg.camera["height"])
                )
            else:
                depth, color = camera.get_frames()
                if depth is None or color is None:
                    time.sleep(0.01)
                    continue

            result = pipeline.process(depth, color)
            count += 1

            if count % 30 == 0:
                print(
                    f"[AERIS] frame={count} gesture={result.gesture.name} "
                    f"confidence={result.gesture.confidence:.2f}"
                )

            if not args.headless and cfg.rendering.get("show_window", True):
                cv2.imshow("AERIS Projector Preview", result.frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        if camera is not None:
            camera.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
