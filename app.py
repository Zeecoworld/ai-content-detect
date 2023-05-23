from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import json
import requests




app = FastAPI(title="AI CONTENT DECTECTING APP")

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def check_item(request: Request):
        
        return templates.TemplateResponse("base.html", {"request": request})



@app.post("/submit")
async def check_item(request: Request, text: str = Form(...)):
        url = "https://cdapi.goom.ai/api/v1/content/detect"
        payload = json.dumps({"content": text})
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        result_endpoint = response.json()
        # print(text,"eee")
        prob_mark = 0.5
        if result_endpoint["fake_probability"] > prob_mark:
            RR = "AI CONTENT"
        else:
            RR = "HUMAN CONTENT"
        return templates.TemplateResponse("base.html", {"request": request,"RR":RR})