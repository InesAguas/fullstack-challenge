from fastapi import APIRouter, WebSocket
import asyncio

router = APIRouter()

#websocket endpoint
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    """ Websocket endpoint for chatbot.
        When a user connects, it sends the message 'Hello, how can I help you?'
        If the user does not send a message for 5 minutes, the connection is closed.
        If the user sends a message, the chatbot responds with a message that is determined by the next_message_generator function.
    """
    
    await websocket.accept()
    await asyncio.sleep(1)
    await websocket.send_text("Hello, how can I help you?")
    try:
        while True:
            data = await asyncio.wait_for(websocket.receive_text(), timeout=300)
            await asyncio.sleep(2)
            msg = next_message_generator(data)
            await websocket.send_text(msg)
    except asyncio.TimeoutError:
        await websocket.send_text("Closing connection due to inactivity")
        await websocket.close()
    except Exception:
        print("Connection closed by client")



def next_message_generator(msg: str):
    """Small function to determine the message to send.
    """
    if "hello" in msg.lower() or "hi" in msg.lower() or "hey" in msg.lower():
        return "Hello, how can I help you?"
    elif "bye" in msg.lower() or "goodbye" in msg.lower():
        return "Goodbye, have a good day!"
    elif "late" in msg.lower() and "order" in msg.lower():
        return "I'm sorry to hear that. I will check your order and get back to you."
    elif "wrong" in msg.lower() and "order" in msg.lower():
        return "I'm sorry to hear that, we will send you the correct order as soon as possible."
    else:
        return "Let me check that for you."
