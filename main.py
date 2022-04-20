from fastapi import FastAPI
import user_api

app = FastAPI()

app.include_router(user_api.router)


@app.get('/')
def root_method():
    return {"msg": "Welcome to Harshit's Blog"}