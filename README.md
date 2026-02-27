# FastAPI

This is a backend API for a catalogue of products.

- **Framework:** FastAPI 0.129+
- **Database:** MySQL 8.0
- **ORM:** SQLModel (SQLAlchemy + Pydantic)
- **Authentication:** JWT with Argon2 password hashing
- **Python:** 3.12+

## Project Structure

```
├── api/
│   ├── deps.py          # Shared dependencies (auth, DB session)
│   └── routes/          # API endpoints
├── core/
│   ├── config.py        # Settings and configuration
│   ├── db.py            # Database connection
│   └── security.py      # Password hashing, JWT
├── crud/                # Database operations
├── models/              # SQLModel schemas
├── enums/               # Enumerations
└── tests/               # Test suites
```

Entities:
- User
- Product
- Category

This should work with [spindulinis/remix](https://github.com/spindulinis/remix) frontend.

### To start the application

`uv run fastapi dev main.py`

### To run the tests

`uv run pytest`