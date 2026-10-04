from __future__ import annotations


class PowerController:
    def __init__(self):
        self.mode = "balanced"

    def set_mode(self, mode: str):
        if mode not in {"performance", "balanced", "powersave"}:
            raise ValueError("mode must be performance, balanced, or powersave")
        self.mode = mode
