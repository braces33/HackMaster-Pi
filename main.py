from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "message": "Hello, World!"}
    )

@app.get("/Wi-Fi/wordlist-generator", response_class=HTMLResponse)
def read_wordlist_generator(request: Request):
    return templates.TemplateResponse(
        "Wi-Fi/wordlist-generator.html", 
        {"request": request, "message": "Wordlist Generator"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=4000)