import os
from dotenv import load_dotenv
from frontend import ExpectingMotherBotFrontend
from backend import ExpectingMotherBotBackend

# Load environment variables from the .env file
load_dotenv()

# Fetch the API key from environment variables (make sure GEMINI_API_KEY is set in .env file)
api_key = os.getenv("GEMINI_API_KEY")

# Initialize backend and frontend
if api_key:
    bot_backend = ExpectingMotherBotBackend(api_key)
else:
    print("API Key is missing. Please check your .env file.")
    exit(1)

bot_frontend = ExpectingMotherBotFrontend(bot_backend)

# Run the Tkinter window's main event loop
bot_frontend.window.mainloop()
