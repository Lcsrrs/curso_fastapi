import asyncio
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.routers import auth, todos, users
from fastapi_zero.schemas import Message

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/ola-mundo/', response_class=HTMLResponse, status_code=HTTPStatus.OK)
async def ola_mundo():
    return """
    <html>
        <head>
                <title>olá mundo</title>
        </head>
        <body>
                <h1>olá mundo</h1>
        </body>
    </html>
    """
