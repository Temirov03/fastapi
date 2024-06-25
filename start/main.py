from fastapi import FastAPI,Query
from enum import Enum
from pydantic import BaseModel,Field

app = FastAPI()

class Image(BaseModel):
    url : str = Field(pattern="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)")
    name : str


class Item(BaseModel):
    name : str
    description : str  = Field(default =None, title="Desciption of an item", min_length="60")
    price : float = Field(gt=0, description="Price of an item")
    tax : float = None
    tags: list[str] = []
    image : Image =None


@app.post("/item/")
async def create_item(item :Item):

    for tag in item.tags:
        print(tag)
    return item


@app.put("/item/{item_id}")
async def create_item(item_id :int, item:Item, search: str=None):
    if search:
        return "Searched"
    return {"item_id":item_id,**item.dict()}


























#
# class UserType(str, Enum):
#     admin = 'admin'
#     superuser = "superuser"
#     regular = 'regular'
#
#
# @app.get("/role/{user_type}")
# async def get_user(user_type: UserType):
#     if user_type == UserType.admin:
#         return {"text": "Hello UserMister"}
#     elif user_type is UserType.superuser:
#         return {"text": "Nurbek nima gap"}
#     else:
#         return {"text": "Kadom murot"}
#
#
# @app.get("/user/1")
# async def get_user():
#     return {"id": "Hello User"}
#
#
# @app.get("/user/{user_id}")
# async def get_user(user_id: int):
#     return {"id": user_id}

# @app.get("/news/feed")
# async def news_feed(search: str):
#     return {"news": ["New1", "New2"], "search_key":search}
