from fastapi import APIRouter, Depends
from ..Schemas.chat_sessionSchema import ChatSession
from ..Services.ChatBotService import ChatBotService

router = APIRouter()

@router.post("/chatbot")
async def chat_with_bot(session: ChatSession, service: ChatBotService = Depends()):
    return service.process_chat_session(session)
