import fastapi
import requests
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse

app = fastapi.FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])
pages = Jinja2Templates(directory="templates")


class NoCacheFileResponse(FileResponse):
    def __init__(self, path: str, **kwargs):
        super().__init__(path, **kwargs)
        self.headers["Cache-Control"] = "no-cache"


@app.get("/", response_class=HTMLResponse)
async def root(request: fastapi.Request):
    r = requests.get("https://openlibrary.org/trending/daily.json")
    j = r.json()
    return pages.TemplateResponse(
        "index.html", {"request": request, "books": j["works"]}
    )


@app.get("/static/{path:path}")
async def static(path: str):
    return NoCacheFileResponse(f"./static/{path}")
