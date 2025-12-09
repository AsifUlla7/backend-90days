from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def check_health():
    return {"status": "ok"}

@app.get("/hello/")
async def greet(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@app.get("/time")
async def get_time():
    from datetime import datetime
    return {"current_time": datetime.utcnow().isoformat()}