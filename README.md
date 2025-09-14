# Visitor Counter API (PostgreSQL Edition)

Track GitHub repository visits and show them as a shields.io badge.

## Features

- `/hit?repo=repo-name` → Increments and stores visit count
- `/badge?repo=repo-name` → Returns shields-compatible JSON badge
- Uses PostgreSQL (Render Free Tier compatible)
- One backend for all your repos

## Deployment on Render (Free Tier)

1. Push this project to a new GitHub repo.
2. Go to https://render.com → New Web Service.
3. Choose 'Deploy from GitHub' → Select this repo.
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
6. Add environment variable `DATABASE_URL` from your Render PostgreSQL service.
7. Deploy!

## Usage

Once deployed, in your README of any GitHub repo:

```markdown
![Visitors](https://your-render-url.onrender.com/badge?repo=samaira)
```
