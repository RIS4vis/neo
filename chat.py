import openai
import json
import os

class ChatInterface:
    def __init__(self):
        self.conversation_history = []
        # Initialize OpenAI GPT 
        self.model = 'gpt-3.5-turbo'  # Change as needed
        self.api_key = os.getenv('OPENAI_API_KEY')

    def chat(self, user_input):
        self.conversation_history.append({'role': 'user', 'content': user_input})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.conversation_history,
            api_key=self.api_key
        )
        bot_response = response['choices'][0]['message']['content']
        self.conversation_history.append({'role': 'assistant', 'content': bot_response})
        return bot_response

    def get_conversation_history(self):
        return self.conversation_history

    def voice_chat(self):
        # Implement voice chat functionality using speech recognition and text-to-speech
        pass

if __name__ == '__main__':
    chat_interface = ChatInterface()
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = chat_interface.chat(user_input)
        print(f'NEO: {response}')