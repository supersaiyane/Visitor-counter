from fastapi import FastAPI, Request, Query, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import crud, models, database
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Visitor Counter API")
templates = Jinja2Templates(directory="templates")

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

@app.get("/admin", response_class=HTMLResponse)
def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    repo_counts = crud.get_all_counts(db)
    return templates.TemplateResponse("admin.html", {"request": request, "repos": repo_counts})

@app.post("/webhook/github")
async def github_webhook(request: Request, db: Session = Depends(get_db)):
    payload = await request.json()
    repo_name = payload.get("repository", {}).get("name", "unknown")
    crud.increment_count(db, repo_name)
    return {"message": f"Ping received from {repo_name}"}
