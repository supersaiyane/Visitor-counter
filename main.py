from fastapi import FastAPI, Query, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app import crud, models, database
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Visitor Counter API")

@app.get("/hit")
def hit(repo: str = Query(...), db: Session = Depends(get_db)):
    count = crud.increment_count(db, repo)
    return {"repo": repo, "visits": count}

@app.get("/badge")
def badge(repo: str = Query(...), db: Session = Depends(get_db)):
    count = crud.get_count(db, repo)
    return JSONResponse(content={
        "schemaVersion": 1,
        "label": "Visitors",
        "message": str(count),
        "color": "brightgreen"
    })