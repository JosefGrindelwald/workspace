import os
import argparse
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Please set it in a .env file."
    )

# Create argument parser
parser = argparse.ArgumentParser(
    description="Simple command-line interface to Google's Gemini API"
)
parser.add_argument(
    "user_prompt",
    type=str,
    help="The prompt/question you want to send to Gemini"
)

# Parse command line arguments
args = parser.parse_args()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Use the user-provided prompt from command line
prompt = args.user_prompt

# Call the Gemini API
response = client.models.generate_content(
    model="gemini-2.5-flash",           # oder "gemini-1.5-flash" je nach Verfügbarkeit 2026
    contents=prompt
)

# Ensure usage metadata exists
if response.usage_metadata is None:
    raise RuntimeError(
        "No usage metadata returned. The API request may have failed."
    )

# Print token usage
print(f"Prompt tokens:  {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# Print the response text
print("\nResponse:")
print(response.text)
