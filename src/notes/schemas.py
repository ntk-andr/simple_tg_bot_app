from pydantic import BaseModel


class ShortNotesSchema(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True


class CategoriesSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
