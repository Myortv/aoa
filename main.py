from fastapi import FastAPI

from routers import anonim_room


app = FastAPI(
    title='aoa'
)

app.include_router(anonim_room.router)
