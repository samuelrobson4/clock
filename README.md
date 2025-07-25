# clock
IoT clock
I'm building a smart kitchen assistant that uses voice input, GPT-4, and a web UI to guide users through cooking recipes step by step.

## 🔧 Core Components:
- Voice input using Whisper (transcribes user speech)
- OpenAI GPT-4o for recipe logic, step tracking, and timer interaction
- Web UI showing:
  - Real-time clock
  - List of active named timers (e.g., "noodles", "oven")
  - Buttons to trigger recipe commands like “next step” or “repeat”
- Backend with REST API to:
  - Add timers
  - Query timers
  - Remove timers
  - Get current recipe step or GPT response

## 🧠 GPT Logic:
- User can say things like:
  - “Set a 10-minute timer for the rice”
  - “What’s the next step?”
  - “How long is left on the oven?”
- GPT should:
  - Parse those commands
  - Call internal functions (not just respond with text)
  - Maintain step context in recipe progression

## 🗂️ Desired Folder Structure:
smart_kitchen_assistant/
├── backend/
│   ├── app.py               # Main FastAPI server
│   ├── gpt_handler.py       # GPT prompt formatting + memory
│   ├── whisper_handler.py   # Audio to text with Whisper
│   ├── timer_manager.py     # Named timer logic (add/remove/query)
│   ├── tts_handler.py       # (Optional) Text-to-speech
│   └── esp_bridge.py        # (Optional) Interface with ESP32 device
├── ui/
│   ├── main.py              # Streamlit UI with clock + timers
│   └── components/          # Modular UI widgets
├── requirements.txt

## 💡 Specific Tasks:
1. Build `timer_manager.py`:
   - Add, remove, query named timers
   - Support duration in seconds or minutes
   - Should support multiple concurrent timers
   - Return remaining time as timedelta or formatted string

2. Build `app.py` (FastAPI preferred):
   - `/add_timer` (POST): takes name and duration
   - `/get_timers` (GET): returns all active timers and remaining time
   - `/remove_timer` (POST): ends a specific timer

3. Build `ui/main.py` with Streamlit:
   - Real-time digital clock at top
   - Show list of current timers
   - Buttons for:
     - “Next step”
     - “Repeat step”
     - “Status check” (e.g., query all timers)

4. GPT Prompt Flow:
   - Receives text input (from Whisper or UI)
   - Determines if the user is asking about:
     - Recipe progression (e.g., next step)
     - Timer management (e.g., set/query/delete)
   - Calls relevant backend functions and forms a friendly spoken/text response

5. Finally:
   - Add `tts_handler.py` using pyttsx3 or edge-tts
   - Add `esp_bridge.py` for ESP32 (e.g., send responses over MQTT or HTTP)

## ✅ Goals:
- Fully modular and testable backend
- Real-time interactive UI
- Clean integration of GPT logic with function calls
- Code should be well-commented and easily extendable

Start by generating the `timer_manager.py` file and the backend server with FastAPI. Then scaffold the Streamlit UI. Prioritize modular code and testable components.
