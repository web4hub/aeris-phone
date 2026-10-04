from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from ai.gesture_recognition import detect_gesture
from ai.lmlm_core import LmlmAI
from reconstruction.mesh_builder import build_mesh
from rendering.lightfield_renderer import render_to_projector
from rendering.interaction_effects import add_touch_effects


@dataclass
class PipelineResult:
    frame: np.ndarray
    gesture: object
    mesh: object


class AERISPipeline:
    def __init__(self, config, ai=None):
        self.config = config
        self.ai = ai or LmlmAI(
            endpoint=config.ai.get("endpoint", ""),
            model=config.ai.get("model", "lmlm-aeris"),
            timeout=float(config.ai.get("timeout_seconds", 5)),
        )

    def process(self, depth, color):
        intrinsics = self.config.camera["intrinsics"]
        mesh = build_mesh(
            depth,
            color,
            intrinsics,
            depth_scale=float(self.config.camera.get("depth_scale", 0.001)),
        )
        gesture = detect_gesture(
            depth,
            threshold_mm=int(self.config.interaction.get("depth_threshold_mm", 900)),
            min_pixels=int(self.config.interaction.get("min_hand_pixels", 300)),
        )
        frame = render_to_projector(
            mesh,
            tuple(self.config.rendering["projector_resolution"]),
            int(self.config.rendering.get("point_size", 2)),
        )
        if gesture.center:
            add_touch_effects(
                frame,
                [gesture.center],
                int(self.config.interaction.get("effect_radius", 14)),
            )
        return PipelineResult(frame=frame, gesture=gesture, mesh=mesh)
