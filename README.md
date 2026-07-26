# Physics Quiz Embed

A minimal Flask app that displays a quiz in an iframe on your own domain.
The source URL is shown openly in the page header (not hidden) — this is a
transparent embed, not a proxy.

## Files
- `main.py` — Flask app + entrypoint
- `templates/index.html` — page with the iframe embed
- `requirements.txt` — Python deps (Flask)
- `Dockerfile` — Python 3.12.1 container for Render

## Deploy on Render (free Web Service)
1. Push this repo to GitHub.
2. On Render: New → Web Service → connect the repo.
3. Environment: **Docker** (Render auto-detects the Dockerfile).
4. No extra env vars needed — `PORT` is set automatically by Render.
5. Deploy. Your quiz will be live at `https://<your-service>.onrender.com/`.

## Changing the quiz URL
Edit `QUIZ_URL` at the top of `main.py`.
