import time
from datetime import timedelta

import importlib.util
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parents[1] / "smart_kitchen_assistant" / "backend"
spec = importlib.util.spec_from_file_location(
    "timer_manager", BACKEND_DIR / "timer_manager.py"
)
timer_manager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(timer_manager)
TimerManager = timer_manager.TimerManager


def test_add_and_query_timer():
    mgr = TimerManager()
    mgr.add_timer('eggs', 2)
    timers = mgr.get_all_timers()
    assert 'eggs' in timers
    remaining = timers['eggs']
    assert timedelta(seconds=0) < remaining <= timedelta(seconds=2)


def test_remove_timer():
    mgr = TimerManager()
    mgr.add_timer('tea', 5)
    assert mgr.remove_timer('tea') is True
    assert 'tea' not in mgr.get_all_timers()
    assert mgr.remove_timer('tea') is False


def test_timer_expiration():
    mgr = TimerManager()
    mgr.add_timer('quick', 1)
    time.sleep(1.1)
    timers = mgr.get_all_timers()
    assert 'quick' not in timers
