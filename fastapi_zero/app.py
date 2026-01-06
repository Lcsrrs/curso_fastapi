from fastapi import FastAPI

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá mundo'}