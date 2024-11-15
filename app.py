from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

app = FastAPI()
from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
