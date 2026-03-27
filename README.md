# GitHub Cloud Connector

A modular backend service to integrate with GitHub's API

## Getting Started

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or `pip`

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd aventisia-assignment
   ```

2. **Setup virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Mac: source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

### Running the Application

Navigate to the `backend` directory and start the server using `uvicorn`:

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
