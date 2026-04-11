from fastapi import FastAPI
from env import SmartClassroomEnv

app = FastAPI()

env = SmartClassroomEnv()


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/reset")
def reset():
    state, _ = env.reset()
    return {"state": state.tolist()}


@app.post("/step")
def step(action: dict):

    act = action.get("action", None)

    state, reward, done, truncated, info = env.step(act)

    return {
        "state": state.tolist(),
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }