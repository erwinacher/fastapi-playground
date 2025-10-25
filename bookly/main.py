from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"status": "OK", "response": "Hello" }


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"status": "OK", "response": f"Hello, {name}"}

