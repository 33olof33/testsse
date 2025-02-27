from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import datetime

app = FastAPI()

async def event_generator():
    while True:
        yield f"data: {datetime.datetime.now().isoformat()}\n\n"
        await asyncio.sleep(1)  # Отправка данных каждую секунду

@app.get("/sse")
async def sse_endpoint():
    return StreamingResponse(event_generator(), media_type="text/event-stream")