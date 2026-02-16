from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GenReq(BaseModel):
    model: str | None = None
    prompt: str
    n: int | None = 1
    size: str | None = "1024x1024"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/images/generations")
def gen(req: GenReq):
    return {"worker": "fake", "prompt": req.prompt, "n": req.n, "size": req.size, "data": ["<fake_image>"]}
