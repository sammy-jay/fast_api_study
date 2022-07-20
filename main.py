from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post('/items/{item_id}')
def create_item(item: Item, item_id: str):
    item_dict = item.dict()
    print(item_dict)
    return {
        "item": item,
        "item_id": item_id
    }
