from fastapi import FastAPI
import random

app = FastAPI()

state = {"students": 30, "temperature": 25}

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    state["students"] = random.randint(20, 40)
    state["temperature"] = random.randint(22, 35)
    return state

@app.post("/step")
def step(action: dict):
    reward = random.random() * 10
    return {
        "students": state["students"],
        "temperature": state["temperature"],
        "reward": reward,
        "done": False
    }