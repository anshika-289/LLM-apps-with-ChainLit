from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from src.prompt import system_instruction
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",   
    temperature=0
)

messages = [
    SystemMessage(content=system_instruction)
]

def ask_order(messages, temperature=0):
    response = llm.invoke(messages)
    return response.content
