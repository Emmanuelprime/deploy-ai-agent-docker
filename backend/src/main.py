from fastapi import FastAPI
import os

app = FastAPI()

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("API_KEY was not set")
@app.get("/")
def read_index():
    return {"hello": f"world again {API_KEY}"}

