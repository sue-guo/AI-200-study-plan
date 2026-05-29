import asyncio

from fastapi import FastAPI
from pydantic import BaseModel

from config import get_settings


app = FastAPI(title="AI-200 Day 2 API")


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    answer: str
    used_endpoint: str


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/config")
async def config() -> dict[str, str | int]:
    settings = get_settings()
    return settings.public_view()


@app.post("/fake-chat")
async def fake_chat(request: PromptRequest) -> PromptResponse:
    settings = get_settings()
    await asyncio.sleep(0.3)

    return PromptResponse(
        answer=f"Pretend model answer for: {request.prompt}",
        used_endpoint=settings.fake_model_endpoint,
    )

