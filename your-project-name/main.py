import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Please set it in a .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)

prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

# Call the Gemini API
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# Ensure usage metadata exists
if response.usage_metadata is None:
    raise RuntimeError(
        "No usage metadata returned. The API request may have failed."
    )

# Print token usage
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# Print the response text
print("Response:")
print(response.text)
