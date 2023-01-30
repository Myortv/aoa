from fastapi import HTTPException

from .utils import DatabaseManager as DM
from utils.criptography import generate_starter_key

from models.room import RoomOut, RoomIn

@DM.make_async()
async def create_room(room: RoomIn, conn=None):
    result = await conn.fetchrow(
        'insert into '
        'rooms(description, starter_key, parent_id) '
        'values '
        '($1, $2, $3) '
        'returning * ',
        room.parent_id,
        generate_starter_key(),
        room.parent_id,
    )
    if not result:
        raise HTTPException(status_code=500, detail='DB errror, data not saved!')
    room = RoomOut(**result)
    return room
    