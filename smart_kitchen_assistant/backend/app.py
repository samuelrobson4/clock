from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import timedelta
from .timer_manager import TimerManager

app = FastAPI(title="Smart Kitchen Assistant API")

# Initialize timer manager
manager = TimerManager()

class TimerRequest(BaseModel):
    name: str
    duration: int  # seconds

class RemoveRequest(BaseModel):
    name: str

@app.post("/add_timer")
async def add_timer(req: TimerRequest):
    try:
        manager.add_timer(req.name, req.duration)
        return {"status": "ok"}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.get("/get_timers")
async def get_timers():
    timers = manager.get_all_timers()
    # Format as seconds remaining
    return {
        name: remaining.total_seconds()
        for name, remaining in timers.items()
    }

@app.post("/remove_timer")
async def remove_timer(req: RemoveRequest):
    if not manager.remove_timer(req.name):
        raise HTTPException(status_code=404, detail="Timer not found")
    return {"status": "removed"}
