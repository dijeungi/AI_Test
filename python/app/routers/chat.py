# app/routers/chat.py
from fastapi import APIRouter, Body
from app.llm_chain import generate_reply
from app.models import get_character_prompt

router = APIRouter(prefix="/chat")

@router.post("/reply")
def chat_with_deceased(
    data: dict = Body(...)
):
    user_id = data["user_id"]
    user_input = data["user_input"]
    response = generate_reply(user_id, user_input)
    return {"response": response}
