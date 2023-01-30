from typing import List

from fastapi import APIRouter

from models.room import RoomIn, RoomOut

from dbmaster.room import create_room

router = APIRouter()

@router.post('/room', response_model=RoomOut)
async def post_room(room: RoomIn):
	result = await create_room(room)
	return result

@router.get('/rooms/', response_model=List[RoomOut])
def get_rooms():
	result = await get_rooms_by_time()
	return result
