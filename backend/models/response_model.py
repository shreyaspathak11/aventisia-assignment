from pydantic import Field
from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

# T represents the type of the 'data' field
T = TypeVar("T")

class SuccessResponse(BaseModel, Generic[T]):
    """
    Standardized success response model for all API endpoints.
    Ensures consistent structure for the frontend.
    """
    status: int = Field(default=200, description="HTTP status code")
    success: bool = Field(default=True, description="Indicates if the request was successful")
    message: str = Field(default="Request successful", description="Human-readable message")
    data: Optional[T] = Field(default=None, description="Response data")

class ErrorResponse(BaseModel):
    """
    Standardized error response model for all API exceptions.
    """
    status: int = Field(default=500, description="HTTP status code")
    success: bool = Field(default=False, description="Indicates if the request was successful")
    message: str = Field(default="Request failed", description="Human-readable error message")
    error_details: Optional[Any] = Field(default=None, description="Detailed error information")