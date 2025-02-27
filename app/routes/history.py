import json
from fastapi import APIRouter, HTTPException, Depends, status, Request, Response
from loguru import logger
from models.history import History
from services.crud.history import add_to_history
from database.database import get_session

history_route = APIRouter(tags=['history'])

@history_route.post('/reaction')
async def reaction(request: Request, session=Depends(get_session)):
    body = await request.body()
    data = json.loads(body.decode('utf-8'))
    new_item = History(
        username = data['username'],
        game_title = data['game_title'],
        reaction = data['reaction']
    )
    add_to_history(new_item, session)
    return 200
