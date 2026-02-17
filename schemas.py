from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    content: str = Field(min_length=5)
    author: str = Field(min_length=3, max_length=20)


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
    profile_pic: str
