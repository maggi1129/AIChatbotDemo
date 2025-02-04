from openai import OpenAI
import random

class DSAChatbot:
    def __init__(self):
        # LangDB API configuration
        self.api_base = "https://api.us-east-1.langdb.ai"
        self.api_key = "YOUR_LANGDB_API_KEY"
        self.default_headers = {"x-project-id": "YOUR_PROJECT_ID"}
        
        # Initialize OpenAI client
        self.client = OpenAI(
            base_url=self.api_base,
            api_key=self.api_key,
        )
        
        # Basic responses for common interactions
        self.basic_responses = {
            "hello": ["Hi! I'm your DSA tutor. What would you like to learn today?", 
                     "Hello! Ready to dive into some Data Structures and Algorithms?",
                     "Welcome! I'm here to help you understand DSA concepts."],
            "bye": ["Goodbye! Keep practicing those algorithms!",
                   "See you later! Don't forget to review your data structures!",
                   "Have a great day! Remember, practice makes perfect!"]
        }

    def get_response(self, user_input):
        # Check for basic commands first
        user_input_lower = user_input.lower()
        if user_input_lower in self.basic_responses:
            return random.choice(self.basic_responses[user_input_lower])
        
        try:
            # Prepare messages for the API
            messages = [
                {
                    "role": "system",
                    "content": "You are a DSA educator. Help the user with their queries regarding DSA. Explain concepts in a clear and simple way, using analogies when helpful."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
            
            # Make API call
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7,
                max_tokens=700,
                top_p=1.0,
                extra_headers=self.default_headers
            )
            
            # Extract and return the assistant's reply
            return response.choices[0].message.content
            
        except Exception as e:
            return f"I encountered an error: {str(e)}"

def main():
    chatbot = DSAChatbot()
    print("DSA Tutor: Hi! I'm your AI-powered DSA tutor. I can help you understand Data Structures and Algorithms.")
    print("          Ask me anything about DSA, or type 'bye' to exit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'bye':
            print("DSA Tutor:", chatbot.get_response("bye"))
            break
            
        response = chatbot.get_response(user_input)
        print("DSA Tutor:", response)

if __name__ == "__main__":
    main()
