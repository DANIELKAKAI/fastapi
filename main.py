from typing import Union, Annotated

from fastapi import FastAPI, Header

from schema import Item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/header")
async def test_header(user_agent: Annotated[str | None, Header()] = None):
    return {"user-agent": user_agent}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    print(item)
    return {"item_name": item.name, "item_id": item_id}
