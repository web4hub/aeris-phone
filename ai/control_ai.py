from __future__ import annotations
from .lmlm_core import LmlmAI


def process_ai(mesh, gestures, ai: LmlmAI | None = None):
    """Keep the AI control plane side-effect free for the render pipeline."""
    if ai is not None and gestures:
        ai.respond("Process spatial interaction", {"gesture": gestures})
    return mesh
