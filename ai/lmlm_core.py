from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
import json
import urllib.request


@dataclass
class LmlmResponse:
    text: str
    raw: Any = None


class LmlmAI:
    """Small HTTP boundary for an eventual native LMLM provider."""

    def __init__(self, endpoint: str = "", model: str = "lmlm-aeris", timeout: float = 5.0):
        self.endpoint = endpoint.strip()
        self.model = model
        self.timeout = timeout

    def respond(self, prompt: str, context: Optional[dict] = None) -> LmlmResponse:
        if not self.endpoint:
            return LmlmResponse(f"[LMLM placeholder] {prompt}")
        payload = json.dumps({
            "model": self.model,
            "prompt": prompt,
            "context": context or {},
        }).encode("utf-8")
        request = urllib.request.Request(
            self.endpoint,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            raw = json.loads(response.read().decode("utf-8"))
        text = raw.get("text") or raw.get("response") or str(raw)
        return LmlmResponse(text, raw)
