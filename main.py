from fastapi import FastAPI

from routers import anonim_room
from dbmaster.utils import DatabaseManager

app = FastAPI(
    title='aoa'
)

app.include_router(anonim_room.router)


@app.on_event('startup')
async def start_plugins():
    await DatabaseManager.start(
        'rooms',
    )
