from typing import List
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

class ChatSession(BaseModel):
    """Model for a session of chat messages."""
    api_key: str = Field(..., description="API key for accessing the chatbot service.")
    messages: List[Message] = Field(..., description="List of messages exchanged in the chat session.")

    class Config:
        """Pydantic model configuration."""
        schema_extra = {
            "example": {
                "api_key": "your_openai_api_key_here",
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello, how are you?"
                    },
                    {
                        "role": "assistant",
                        "content": "I'm fine, thank you."
                    }
                ]
            }
        }
