import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions
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

# NEW optional verbose flag
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output"
)

# Parse command line arguments
args = parser.parse_args()

# Create Gemini client
client = genai.Client(api_key=api_key)

prompt = args.user_prompt

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]

# Call the Gemini API
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[available_functions],
    ),
)


# Ensure usage metadata exists
if response.usage_metadata is None:
    raise RuntimeError(
        "No usage metadata returned. The API request may have failed."
    )

# VERBOSE OUTPUT
if args.verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# Always print response text
print("\nResponse:")
if response.function_calls:
    for function_call in response.function_calls:
        print(
            f"Calling function: {function_call.name}({function_call.args})"
        )
else:
    print(response.text)


