# main.py
from fastapi import FastAPI
import os

# Import routes
from routes import health, greeting

app = FastAPI(title="PROJECT_NAME")

# Include routes
app.include_router(health.router)
app.include_router(greeting.router)

@app.get("/")
def read_root():
    username = os.getenv("USER", "Developer")
    return {"message": f"Hello {username} from FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)