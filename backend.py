import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

class ExpectingMotherBotBackend:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)  # Configure Gemini API
        self.model = genai.GenerativeModel("models/gemini-1.5-flash")  # Specify the model
    
    def get_pregnancy_tip(self):
        """Generate a pregnancy tip."""
        prompt = "Give me a helpful tip for expecting mothers."
        result = self.model.generate_content(prompt)
        return result.text if result.text else "Sorry, I couldn't fetch a tip right now."

    def get_nutrition_advice(self, week):
        """Generate nutritional advice based on pregnancy week."""
        prompt = f"Provide nutrition advice for week {week} of pregnancy."
        result = self.model.generate_content(prompt)
        return result.text if result.text else "I couldn't fetch nutrition advice at the moment."

    def get_emotional_support(self):
        """Provide emotional support through generated content."""
        prompt = "What resources are available for emotional support for expecting mothers?"
        result = self.model.generate_content(prompt)
        return result.text if result.text else "I'm having trouble fetching emotional support resources."

    def chat_with_bot(self, user_input):
        """Handle free-form user queries."""
        chat = self.model.start_chat()
        response = chat.send_message(user_input)
        return response.text if response.text else "I'm here to help, but I didn't understand your query."