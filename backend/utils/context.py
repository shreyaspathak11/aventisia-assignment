from contextvars import ContextVar
from typing import Dict, Any, Optional

# ContextVar provides a thread-safe, stateless container for storage of the 
# authenticated user's metadata throughout a single request's lifecycle.
user_context: ContextVar[Optional[Dict[str, Any]]] = ContextVar("user_context", default=None)

def get_current_user_login() -> Optional[str]:
    """
    Retrieves the unique GitHub login (username) from the current request context.
    Returns None if the user context has not been initialized by the AuthMiddleware.
    """
    user = user_context.get()
    return user.get("login") if user else None

def get_user_profile() -> Optional[Dict[str, Any]]:
    """
    Retrieves the complete GitHub user profile dictionary from the request context.
    """
    return user_context.get()
