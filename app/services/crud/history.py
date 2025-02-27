from models.history import History

def add_to_history(new_item: History, session):
    session.add(new_item)
    session.commit()

