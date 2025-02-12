from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage


llm = Ollama(model="llama3.2", request_timeout=120.0)


async def ollama_answer(user_query):
    messages = [ChatMessage(role="user", content=user_query)]
    responce = ""
    try:        
        responce_stream = llm.stream_chat(messages=messages)

        for chunk in responce_stream:
            responce += chunk.delta
        return responce
    except Exception as e:
        return str(e)
        