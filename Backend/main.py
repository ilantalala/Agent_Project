from fastapi import FastAPI, HTTPException
from models import ChatRequest
from ai import chat
from excel_logger import log_conversation
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Hebrew Delivery AI Agent")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      
    allow_credentials=True,
    allow_methods=["*"],      
    allow_headers=["*"],     
)
@app.post("/chat")
def chat_endpoint(payload: ChatRequest):
    if not payload.messages:
        raise HTTPException(status_code=400, detail="No messages provided")

    messages = [
        {"role": m.role, "content": m.content}
        for m in payload.messages
    ]

    reply = chat(
        messages=messages,
        model=payload.model,
        system_prompt=payload.system_prompt
    )

    full_conversation = "\n".join(
        [f"{m.role}: {m.content}" for m in payload.messages] +
        [f"assistant: {reply}"]
    )

    try:
        log_conversation(
            name=payload.name or "Unknown",
            phone=payload.phone or "Unknown",
            conversation=full_conversation
        )
    except Exception as e:
        print("Excel logging failed:", e)

    return {"reply": reply}
