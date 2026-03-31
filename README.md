# GitHub Cloud Connector and Knowledge Base

A production-grade full-stack application designed to integrate with the GitHub REST API. This system provides a unified interface for managing repositories, issues, and pull requests with enterprise-standard security and modular architecture.

---

## Key Features

*   **GitHub OAuth 2.0 Integration**: Secure authentication flow utilizing the official GitHub OAuth handshake, replacing the need for manual Personal Access Token entry.
*   **Knowledge Base Interface**: A responsive React application providing an intuitive grid-based management layer for GitHub data.
*   **Modular API endpoints**: Dedicated routes for fine-grained operations including branch management, isolated file commits, and Pull Request orchestration.
*   **Standardized Error Handling**: A centralized utility that transforms external API status codes and validation messages into actionable JSON responses.

---

## System Architecture

The project utilizes a decoupled architecture to ensure scalability and maintainability:

*   **Backend Service**: Developed with Python and FastAPI, the backend acts as an authenticated proxy to GitHub. It follows the Service-Controller-API pattern for clear separation of concerns.
*   **Frontend Application**: A React-based single-page application (SPA) focused on visual fidelity and optimized user workflows, leveraging Tailwind CSS for styling.

---

## Installation and Setup

### Backend (FastAPI)
1.  Navigate to the `backend/` directory.
2.  Initialize a virtual environment: `python -m venv venv`.
3.  Install required packages: `pip install -r requirements.txt`.
4.  Configure the `.env` file with your GitHub Application credentials (see [Backend Documentation](backend/README.md)).
5.  Execute the service: `uvicorn main:app --reload`.

### Frontend (React)
1.  Navigate to the `frontend/` directory.
2.  Install dependencies: `npm install`.
3.  Launch the development server: `npm run dev`.

---

## Technical Stack

| Category | Technology |
| :--- | :--- |
| **Logic (Backend)** | Python 3.x, FastAPI |
| **Communication** | HTTPX (Async HTTP Client) |
| **Interface (Frontend)** | React, Tailwind CSS |
| **Authentication** | OAuth 2.0 (Authorization Code Grant) |

---

Developed as a modern cloud connectivity solution.
