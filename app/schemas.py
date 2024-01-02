from pydantic import BaseModel


class ItemBase(BaseModel):
    value: str


class ItemCreate(ItemBase):
    value: str


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
