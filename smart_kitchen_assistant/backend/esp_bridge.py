import requests
from typing import Optional

class ESPBridge:
    """Send messages to an ESP32 device over HTTP."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def send_message(self, path: str, payload: Optional[dict] = None) -> bool:
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            resp = requests.post(url, json=payload or {})
            return resp.status_code == 200
        except Exception:
            return False
