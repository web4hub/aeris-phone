from __future__ import annotations
import numpy as np

try:
    import sounddevice as sd
except ImportError:
    sd = None


class Microphone:
    def __init__(self, samplerate: int = 16000, channels: int = 1):
        self.samplerate = samplerate
        self.channels = channels

    def record(self, duration: float = 1.0) -> np.ndarray:
        if sd is None:
            raise RuntimeError("sounddevice is not installed")
        if duration <= 0:
            return np.empty(0, dtype=np.float32)
        audio = sd.rec(
            int(duration * self.samplerate),
            samplerate=self.samplerate,
            channels=self.channels,
            dtype="float32",
        )
        sd.wait()
        return np.asarray(audio).reshape(-1)
