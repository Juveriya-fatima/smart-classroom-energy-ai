from fastapi import FastAPI
from env import SmartClassroomEnv

app = FastAPI()

env = SmartClassroomEnv()

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: dict):
    act = action.get("action", None)

    state, reward, done, info = env.step(act)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }