from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass
class AERISConfig:
    camera: dict
    rendering: dict
    interaction: dict
    ai: dict
    system: dict


def load_config(path="config/config.yaml") -> AERISConfig:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return AERISConfig(**data)
