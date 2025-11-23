from datetime import datetime,timezone
from sqlmodel import Field, SQLModel,DateTime
from typing import Optional

def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)


# for input validation
class ChatMessagePayload(SQLModel):
    message: str 

# for storing in db
class ChatMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str 
    created_at: datetime = Field(default_factory=get_utc_now,sa_type=DateTime(timezone=True),primary_key=False,nullable=False)


class ChatMessageList(SQLModel):
    message: str
    created_at: datetime = Field(default=None)