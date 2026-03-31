# GitHub Cloud Connector Backend

This backend service is a FastAPI-based application that manages the orchestration between the GitHub REST API and the frontend client. It provides secure authentication via OAuth 2.0 and modular endpoints for repository management.

---

## Architectural Pattern: Service-Controller-API

This service adheres to a strictly decoupled architecture:
1.  **Service Layer**: Encapsulates raw HTTP communication with the GitHub REST API.
2.  **Controller Layer**: Implements business logic, orchestration of multiple services, and error handling transformation.
3.  **API Layer (Routers)**: Defines the JSON endpoints and executes the FastAPI dependency injection flow.

---

## OAuth 2.0 Authentication

The backend handles the complete authorization code flow for GitHub:
1.  **`/api/v1/auth/login`**: Initiates the handshake by generating a unique authorization URL and redirecting the client.
2.  **`/api/v1/auth/callback`**: Processes the incoming code, exchanges it for a permanent access token via GitHub's OAuth service, and returns the result as structured JSON.

All subsequent calls require an Authorization header:
`Authorization: Bearer <access_token>`

---

## API Endpoints

### Authentication
*   `GET /api/v1/auth/login`: Authorization start point.
*   `GET /api/v1/auth/callback`: Token exchange hook (internal).

### GitHub Operations
*   `GET /api/v1/github/repos`: Lists the authenticated user's repositories.
*   `GET /api/v1/github/issues/{repo}`: Lists issues for a specific repository.
*   `POST /api/v1/github/issues`: Creates a new repository issue.
*   `GET /api/v1/github/commits/{repo}`: Fetches total commit history.
*   `POST /api/v1/github/create-branch`: Creates a new branch from a specified base branch.
*   `POST /api/v1/github/create-file`: Pushes a new file with specified content to a branch.
*   `POST /api/v1/github/create-pull-request`: Orchestrates the creation of a Pull Request.

---

## Configuration

Environmental variables are managed via a `.env` file in the root backend directory:

```env
GITHUB_CLIENT_ID=<Your_Application_Client_ID>
GITHUB_CLIENT_SECRET=<Your_Application_Client_Secret>
```

---

## Security and Performance

*   **`AuthMiddleware`**: Intercepts all requests (excluding auth routes) to verify the Bearer token and populate a stateless `user_context`.
*   **Shared HTTP Client**: A single `httpx.AsyncClient` is initialized during the `lifespan` of the FastAPI application for efficient resource pooling.
*   **Standardized Responses**: All successful calls return a `SuccessResponse` model, while failures utilize a unified `ErrorResponse` model for client-side consistency.

---

Developed for high-performance cloud connectivity.
