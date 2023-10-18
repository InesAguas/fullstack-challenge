from fastapi import APIRouter, WebSocket
import asyncio

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello, how can I help you?")

    while True:
        data = await websocket.receive_text()
        await asyncio.sleep(2)
        await websocket.send_text(f"Message text was: {data}")
        
