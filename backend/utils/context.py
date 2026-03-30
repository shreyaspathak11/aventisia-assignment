from contextvars import ContextVar
from typing import Dict, Any, Optional

# Global context for the authenticated GitHub user
user_context: ContextVar[Optional[Dict[str, Any]]] = ContextVar("user_context", default=None)

def get_current_user_login() -> Optional[str]:
    """Helper to get the current user's login name from context."""
    user = user_context.get()
    return user.get("login") if user else None

def get_user_profile() -> Optional[Dict[str, Any]]:
    """Helper to get the full user profile from context."""
    return user_context.get()
