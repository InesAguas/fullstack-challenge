from fastapi import APIRouter, WebSocket
import asyncio

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    await websocket.accept()
    await asyncio.sleep(1)
    await websocket.send_text("Hello, how can I help you?")
    try:
        while True:
            data = await asyncio.wait_for(websocket.receive_text(), timeout=10)
            await asyncio.sleep(2)
            await websocket.send_text(f"Message text was: {data}")
    except asyncio.TimeoutError:
        await websocket.send_text("Goodbye")
        await websocket.close()
    except Exception:
        print("Connection closed by client")
    
