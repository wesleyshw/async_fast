from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from async_fast.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    # return Message(message="Olá Mundo!")
    return {'message': 'Olá Mundo!'}


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    return """
    <html>
        <head>
            <title>Exercício Aula 02</title>
        </head>
        <body>
            <h1> Olá mundo </h1>
        </body>
    </html>"""
