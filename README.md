# ReachAble

A web application for monitoring the available for API and web endpoints.

## Tech Stack

**Backend**
- Python 3.11+
- FastAPI - web framework
- SQLAlchemy - ORM
- SQLite - database
- APScheduler - periodic endpoint checks
- PyJWT - JWT authentication
- python-telegram-bot - Telegram notifications

**Frontend**
- React 18
- Tailwind CSS
- Axios _ HTTP client
- react-router-dom - routing

## Project Structure

```
ReachAble/
├── backend/
│   ├── main.py          # FastAPI app entry point
│   ├── auth.py          # JWT authentication
│   ├── database.py      # DB connection & session
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── monitor.py       # Endpoint monitoring logic
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── App.jsx
│       ├── pages/       # Login, Dashboard, etc.
│       ├── components/  # Reusable UI components
│       └── api/         # Axios API calls
└── docs/
```
