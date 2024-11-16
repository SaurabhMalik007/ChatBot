# 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

import openai

# Set up your OpenAI API key here
openai.api_key = "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"  # Replace with your actual API key

def chatbot_response(user_input):
    """
    Function to get a response from OpenAI's GPT model (with new API v1.0.0+).
    """
    try:
        # Ensure the required arguments are passed: model and prompt
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Choose the model (e.g., "gpt-3.5-turbo" or "gpt-4")
            prompt=user_input,  # The user's input is the prompt for the model
            max_tokens=150,  # Maximum number of tokens (words) in the response
            temperature=0.7  # Adjusts randomness of the response (0 = deterministic, 1 = random)
        )
        
        # Extract the model's response from the API response
        message = response['choices'][0]['text'].strip()
        return message
    except Exception as e:
        return f"Error: {str(e)}"

def chat():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
