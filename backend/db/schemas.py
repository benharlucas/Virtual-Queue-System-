from typing import List, Optional
from pydantic import BaseModel, Field
import datetime
from fastapi import Body
from typing import List, Union


class UserInfo(BaseModel):
    id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True


class UserCredentials(UserInfo):
    password: str


class EventInfo(BaseModel):
    id: str
    name: str
    description: str
    time_created: Optional[datetime.datetime] = Body(None)
    time_updated: Optional[datetime.datetime] = Body(None)
    user_id: str
    start_time: datetime.datetime
    end_time: datetime.datetime

    class Config:
        orm_mode = True


class SlotInfo(BaseModel):
    start_time: datetime.datetime
    end_time: datetime.datetime
    event_id: str
    participant_limit: int

    class Config:
        orm_mode = True


class Slot(SlotInfo):
    id: int


class ParcipantInfo(BaseModel):
    user_id: str
    event_id: str
    slot_id: int

    class Config:
        orm_mode = True


class Participant(ParcipantInfo):
    id: int
    token: int


class UserRegisteredEventDetails(BaseModel):
    slot: Slot = Field(None, alias='Slot')

    event: Participant = Field(None, alias='Participant')

    class Config:
        orm_mode = True


class ListUserRegisteredEventDetails(BaseModel):
    detail: Union[Slot, Participant] = Field(None, alias='Detail')

    # class Config:
    #     orm_mode = True
