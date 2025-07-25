import streamlit as st
import requests
from datetime import datetime
import time

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="Smart Kitchen Assistant")

# Real-time clock
st.title("🧑‍🍳 Smart Kitchen Assistant")
clock_placeholder = st.empty()

def fetch_timers():
    try:
        resp = requests.get(f"{API_BASE}/get_timers")
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return {}

# Timer display
st.subheader("Active Timers")
timers_container = st.empty()

col1, col2, col3 = st.columns(3)
if col1.button("Next step"):
    st.write("Not implemented yet")
if col2.button("Repeat step"):
    st.write("Not implemented yet")
if col3.button("Status check"):
    st.json(fetch_timers())

while True:
    clock_placeholder.markdown(f"### {datetime.now().strftime('%H:%M:%S')}")
    timers = fetch_timers()
    if timers:
        timers_container.table([
            {"Timer": name, "Seconds left": int(remaining)}
            for name, remaining in timers.items()
        ])
    else:
        timers_container.write("No active timers")
    time.sleep(1)
