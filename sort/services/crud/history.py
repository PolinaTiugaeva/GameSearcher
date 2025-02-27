from loguru import logger
from models.history import History
from sqlmodel import Session, select
from typing import List

def get_recommendations(username: str, session) -> List[str]:
    stament0 = select(History).where(History.username == username)
    games_list = session.exec(stament0).all()
    logger.info(games_list)
    statment1 = select(History.username).where(History.game_title.in_([history.game_title for history in games_list]), History.reaction == 1)
    neighbors_list = session.exec(statment1).all()
    logger.info(neighbors_list)
    statement2 = select(History.game_title).where(History.username.in_(neighbors_list), History.game_title.notin_([history.game_title for history in games_list]), History.reaction == 1)
    recommendations = session.exec(statement2).all()
    logger.info(recommendations)
    session.commit()
    return recommendations

