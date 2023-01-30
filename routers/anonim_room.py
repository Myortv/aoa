from fastapi import APIRouter

router = APIRouter()

@router.get('/test/')
async def test():
	return 'WOW ITS WORKS'