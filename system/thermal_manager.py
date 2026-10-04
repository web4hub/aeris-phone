from __future__ import annotations
import glob


class ThermalManager:
    def __init__(self, limit_c=80.0):
        self.limit_c = float(limit_c)

    def read_temperature(self):
        values = []
        for path in glob.glob("/sys/class/thermal/thermal_zone*/temp"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    values.append(float(f.read().strip()) / 1000.0)
            except (OSError, ValueError):
                pass
        return max(values) if values else None

    def throttling_required(self):
        temp = self.read_temperature()
        return temp is not None and temp >= self.limit_c
