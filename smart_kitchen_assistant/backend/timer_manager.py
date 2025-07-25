from datetime import datetime, timedelta
from typing import Dict, Optional

class Timer:
    """Represents a named countdown timer."""

    def __init__(self, name: str, duration: timedelta):
        self.name = name
        self.duration = duration
        self.start_time = datetime.utcnow()

    @property
    def remaining(self) -> timedelta:
        elapsed = datetime.utcnow() - self.start_time
        remaining = self.duration - elapsed
        return remaining if remaining > timedelta(0) else timedelta(0)

    def is_expired(self) -> bool:
        return self.remaining == timedelta(0)


class TimerManager:
    """Manage multiple named timers."""

    def __init__(self):
        self.timers: Dict[str, Timer] = {}

    def add_timer(self, name: str, duration_seconds: int) -> None:
        if duration_seconds <= 0:
            raise ValueError("Duration must be positive")
        self.timers[name] = Timer(name, timedelta(seconds=duration_seconds))

    def remove_timer(self, name: str) -> bool:
        return self.timers.pop(name, None) is not None

    def get_timer(self, name: str) -> Optional[Timer]:
        timer = self.timers.get(name)
        if timer and timer.is_expired():
            # Auto remove expired timers
            self.timers.pop(name, None)
            return None
        return timer

    def get_all_timers(self) -> Dict[str, timedelta]:
        expired = [n for n, t in self.timers.items() if t.is_expired()]
        for name in expired:
            self.timers.pop(name, None)
        return {name: timer.remaining for name, timer in self.timers.items()}
