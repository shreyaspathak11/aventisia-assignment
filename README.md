# GitHub Cloud Connector

A professional, modular backend service to integrate with GitHub's API. Built with **FastAPI** using a context-aware architecture that automatically identifies the authenticated user.

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
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
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

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## How to Authenticate (PAT)

1. Generate a **Personal Access Token (PAT)** in GitHub settings.
2. In Swagger UI, click the **"Authorize"** button.
3. Enter: `token ghp_your_token_here`
4. All subsequent API calls will automatically identify you and use your repositories.
