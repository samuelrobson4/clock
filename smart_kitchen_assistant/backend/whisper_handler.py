import io
import requests

class WhisperHandler:
    """Transcribe audio using OpenAI Whisper API."""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def transcribe(self, audio_bytes: bytes, filename: str = "audio.wav") -> str:
        files = {"file": (filename, io.BytesIO(audio_bytes), "audio/wav")}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers=headers,
            files=files,
            data={"model": "whisper-1"},
        )
        response.raise_for_status()
        return response.json().get("text", "")
