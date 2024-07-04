# app/models/message.py
from pydantic import BaseModel, Field

class Message(BaseModel):
    """Model for individual messages in a conversation."""
    role: str = Field(..., description="Role of the message sender (e.g., 'user', 'assistant').")
    content: str = Field(..., description="Content of the message.")

    class Config:
        """Pydantic model configuration."""
        schema_extra = {
            "example": {
                "role": "user",
                "content": "Hello, how are you?"
            }
        }
