# Visitor Counter API

Track GitHub repository visits and show them as a shields.io badge.

## Features

- `/hit?repo=repo-name` → Increments and stores visit count
- `/badge?repo=repo-name` → Returns shields-compatible JSON badge
- Works with SQLite (or switch to PostgreSQL easily)
- One backend for all your repos

## Usage

Add this to any GitHub README:

```markdown
![Visitors](https://your-deployment-url/badge?repo=my-repo-name)
```

## Quick Deploy (Railway)

1. Push this project to a GitHub repo
2. Visit [https://railway.app](https://railway.app)
3. Choose "New Project" → "Deploy from GitHub Repo"
4. Done 🎉