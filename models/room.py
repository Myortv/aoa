from typing import List, Optional
from pydantic import BaseModel

class RoomIn(BaseModel):
	parent_id: Optional[int] = None
	desription: Optional[str] = None


class RoomOut(RoomIn):
	id: int
	starter_key: str
	# bans: List[str]

