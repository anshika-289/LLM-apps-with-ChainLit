import chainlit as cl
from langchain.schema import HumanMessage, AIMessage
from src.llm import ask_order, messages


@cl.on_message
async def main(message: cl.Message):
    # Add user message (LangChain format)
    messages.append(HumanMessage(content=message.content))

    # Call Groq LLM
    response = ask_order(messages)

    # Add assistant response
    messages.append(AIMessage(content=response))

    # Send response to Chainlit UI
    await cl.Message(content=response).send()
