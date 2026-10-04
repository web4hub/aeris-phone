from __future__ import annotations
import os


class BatteryMonitor:
    def __init__(self, fallback=100.0):
        self.fallback = float(fallback)

    def read_level(self):
        path = "/sys/class/power_supply/BAT0/capacity"
        try:
            with open(path, "r", encoding="utf-8") as f:
                return float(f.read().strip())
        except (OSError, ValueError):
            return self.fallback
