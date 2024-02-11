from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    een_var = "deze var"
    return templates.TemplateResponse("index.html", {"some_var": een_var, "request": request})


@app.get("/clicked")
async def do_clicked(request: Request):
    random_number = random.randint(0, 100)
    return templates.TemplateResponse("click-response.html", {"request": request, "random_waarde": random_number})
