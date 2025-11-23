from typing import List
from fastapi import APIRouter,Depends
from sqlmodel import Session,select

from api.db import get_session
from .models import ChatMessagePayload,ChatMessage,ChatMessageList

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}


# curl -X POST -H "Content-Type: application/json" -d "{\"message\":\"hello world\"}" http://localhost:8080/api/chat/

@router.post("/", response_model=ChatMessageList)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data = payload.model_dump()
    print(data)

    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    return obj

# curl http://localhost:8080/api/chat/recent/

@router.get("/recent/", response_model=List[ChatMessageList])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    result =  session.exec(query).fetchall()[:10]
    return result