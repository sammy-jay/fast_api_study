from typing import Union
from fastapi import FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get('/items/{item_id}')
def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item['q'] = q
    if not short:
        item['description'] = "This is an amazing item"

    return item


@app.get('/users/{user_id}/items/{item_id}')
def read_user_item(user_id: str, item_id: str, category: str = "all", order: Union[str, None] = None):
    return {
        "user_id": user_id,
        "item_id": item_id,
        "category": category,
        "order": order
    }
