# app/routers/character.py
from fastapi import APIRouter
from app.models import create_character

router = APIRouter(prefix="/character")

@router.post("/create")
async def create_character_endpoint(character: dict):
    # 캐릭터 저장 함수 호출
    response = create_character(character)
    return {"message": "Character created successfully", "data": response}
