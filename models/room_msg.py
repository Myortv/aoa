from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

from .room import RoomOut


class MessageIn(BaseModel):
	parent: Optional[int] = None
	room_id: int
	body: str

class MessageOut(MessageIn):
	id: int
	created_at: datetime


class MessagePage(BaseModel):
	room: RoomOut
	total: int
	page: int
	messages: List[MessageOut]
