from sqlalchemy.orm import Session
from app.models import VisitorCount

def get_count(db: Session, repo: str) -> int:
    counter = db.query(VisitorCount).filter(VisitorCount.repo == repo).first()
    return counter.count if counter else 0

def increment_count(db: Session, repo: str) -> int:
    counter = db.query(VisitorCount).filter(VisitorCount.repo == repo).first()
    if counter is None:
        counter = VisitorCount(repo=repo, count=1)
        db.add(counter)
    else:
        counter.count += 1
    db.commit()
    return counter.count