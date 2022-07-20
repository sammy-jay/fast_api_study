from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "my first python api"}