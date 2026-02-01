import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Check if the API key was found
if api_key is None:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Please create a .env file with your API key:\n"
        "GEMINI_API_KEY='your_api_key_here'"
    )

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Define the prompt
prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

# Generate content using the gemini-2.5-flash model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# Print the model's response
print(response.text)
