from fastapi import FastAPI
import random

app = FastAPI()

state = {}

@app.post("/reset")
def reset():
    global state
    state = {
        "students": random.randint(20, 40),
        "temperature": random.randint(22, 35)
    }
    return state

@app.post("/step")
def step(action: dict):
    reward = random.uniform(0, 10)
    done = False

    return {
        "students": state["students"],
        "temperature": state["temperature"],
        "reward": reward,
        "done": done
    }