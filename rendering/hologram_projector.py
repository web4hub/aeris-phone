from __future__ import annotations
from .lightfield_renderer import render_to_projector


def project_hologram(mesh, resolution=(1280, 720)):
    return render_to_projector(mesh, resolution)
