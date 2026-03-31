from fastapi import HTTPException
from httpx import HTTPStatusError
from utils.logger import logger

def handle_api_error(e: Exception, default_msg: str = "API communication failed"):
    """
    Centralized error handler for all external API interactions.
    Transforms status errors and general exceptions into clean HTTPExceptions.
    """
    try:
        error_data = e.response.json()
        message = error_data.get("message", default_msg)
        
        # Extract detailed validation errors if present (e.g., GitHub PR errors)
        if "errors" in error_data:
            err = error_data['errors'][0]
            field = err.get('field', 'unknown')
            code = err.get('code', 'invalid')
            # Use specific message if present, or fallback to field explanation
            detail_msg = err.get('message', f"The field '{field}' is '{code}'")
            message = f"{message}: {detail_msg}"
            
    except Exception:
        # Fallback if response isn't JSON or message key is missing
        message = default_msg
        
    logger.error(f"API Error ({e.response.status_code}): {e.response.text}")
    raise HTTPException(status_code=e.response.status_code, detail=message)


