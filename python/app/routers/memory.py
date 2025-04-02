# app/routers/memory.py
from fastapi import APIRouter
from app.models import get_all_memories
from app.models import save_memory

router = APIRouter(prefix="/memory")

@router.get("/{user_id}")
def read_memories(user_id: int):
    return get_all_memories(user_id)

@router.post("/add")
async def add_memory(memory: dict):
    # 추억 저장 함수 호출
    response = save_memory(memory)
    return {"message": "Memory saved successfully", "data": response}
