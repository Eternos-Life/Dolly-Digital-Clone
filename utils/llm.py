# TODO: Use this file to generate a response using the LLM. Feel free to modify this file as you see fit.

from typing import List, Dict
from .prompt import get_mock_response

#TODO: Implement the LLM call here. Feel free to change the signature and implementation to your liking.
def generate_response(user_input: str, context: str, chat_history: List[Dict[str, str]]) -> str:
    """
    Generate a response using the LLM based on user input, context, and chat history.
    
    Args:
        user_input (str): The user's question
        context (str): Retrieved context from the vector store
        chat_history (List[Dict[str, str]]): List of previous messages in the conversation
        
    Returns:
        str: Generated response from the LLM
    """
    
    return get_mock_response(user_input, context)