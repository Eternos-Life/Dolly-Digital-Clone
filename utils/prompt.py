#TODO: Store relevant prompts here. Feel free to modify this file as you see fit.

#TODO: This is where you can define the personality of the digital twin and/ or pass in relevant context
SYSTEM_PROMPT = """You are Dolly's digital twin. Please reply to the user's query based on the context provided.
If the user's query is not related to the context, please say that you don't know.
If the user's query is not clear, please ask for more information.
If the user's query is not related to the context, please say that you don't know.
"""

#NOTE: This is just a placeholder for the chat prompt. Feel free to modify this file as you see fit.
def get_chat_prompt(user_query: str, context: str) -> str:
    """
    Generate a prompt for the chat model using the user query and retrieved context.
    
    Args:
        user_query (str): The user's question
        context (str): Retrieved context from the vector store
        
    Returns:
        str: Formatted prompt for the chat model
    """
    return f"""Based on the following context, please answer the user's question:

Context:
{context}

User Question:
{user_query}

Please provide a helpful and accurate response based on the available information."""

def get_mock_response(user_input: str, retrieved_docs: str) -> str:
    """
    Generate a mock response for development/testing purposes.
    
    Args:
        user_input (str): The user's question
        retrieved_docs (str): Retrieved context from the vector store
        
    Returns:
        str: Mock response
    """
    return f"""🤖 [Placeholder] I received your question:
> {user_input}

Using retrieved context:
> {retrieved_docs}

...but I haven't been fully implemented yet!"""

