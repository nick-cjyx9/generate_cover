from fastapi import FastAPI, Response
from generate import draw
app = FastAPI()
@app.get("/get_cover")
def get_cover(title: str):
    cover = draw(title)
    response = Response(content=cover.getvalue(), media_type="image/webp")
    return response
