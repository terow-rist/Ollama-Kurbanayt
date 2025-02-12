from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage


llm = Ollama(model="llama3.2", request_timeout=120.0)


async def ollama_answer(user_query):
    system_instruction = (
        "You are a code generator AI. Always return only pure code without any explanations, "
        "comments, or extra text. If the user asks for HTML, return only HTML. "
        "If they ask for CSS, return only CSS. If they ask for JavaScript, return only JavaScript."
    )

    messages = [
        ChatMessage(role="system", content=system_instruction),
        ChatMessage(role="user", content=user_query),
    ]

    responce = ""
    try:        
        responce_stream = llm.stream_chat(messages=messages)

        for chunk in responce_stream:
            responce += chunk.delta
        return responce
    except Exception as e:
        return str(e)
        