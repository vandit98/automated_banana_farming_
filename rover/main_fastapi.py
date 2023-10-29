from fastapi import FastAPI
from render.engine import Engine

app = FastAPI()

NEAT_CONFIG_PATH = "ai/config.txt"
DEBUG = True
MAX_SIMULATIONS = 1000



@app.get("/")
async def root():
    return {"message": "Welcome to the car simulation API!"}

@app.get("/run_simulation")
async def run_simulation():
    window = Engine(NEAT_CONFIG_PATH, DEBUG, MAX_SIMULATIONS)
    window.run()
    return None
