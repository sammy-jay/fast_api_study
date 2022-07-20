from fastapi import FastAPI

app = FastAPI()


# Order matters
@app.get('/items/me')
def read_user_me():
    return {"user_id": "22"}

@app.get('/items/{item_id}')
async def root(item_id:int):
    return {"message": f"Item ID: {item_id}"}
