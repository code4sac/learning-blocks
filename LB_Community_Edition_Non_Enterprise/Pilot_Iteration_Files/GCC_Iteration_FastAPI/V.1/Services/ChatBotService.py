from ..Models.Chatbot import ChatSession
import openai

class ChatBotService:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def process_chat_session(self, session: ChatSession):
        # Logic to handle chat session with OpenAI's GPT-3
        # Example implementation:
        conversation_history = []
        for message in session.messages:
            conversation_history.append({"role": "user", "content": message.message})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history
            )
            conversation_history.append({"role": "assistant", "content": response.choices[0].message['content']})
        return conversation_history
