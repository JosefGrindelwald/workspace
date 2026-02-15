import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import call_function, available_functions


# ---- Load API key ----
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Please set it in a .env file."
    )


# ---- CLI arguments ----
parser = argparse.ArgumentParser(
    description="Simple command-line interface to Google's Gemini API"
)

parser.add_argument(
    "user_prompt",
    type=str,
    help="The prompt/question you want to send to Gemini"
)

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output"
)

args = parser.parse_args()


# ---- Create Gemini client ----
client = genai.Client(api_key=api_key)

prompt = args.user_prompt

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]

# ---- Initial output ----
if args.verbose:
    print(f"User prompt: {prompt}")

print("\nResponse:")


# ---- AGENT LOOP ----
for _ in range(20):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        ),
    )

    # ---- Verbose token usage ----
    if args.verbose and response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # ---- Add model replies to conversation ----
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    # ---- If model wants to call tools ----
    if response.function_calls:

        function_responses = []

        for function_call in response.function_calls:

            function_call_result = call_function(
                function_call,
                verbose=args.verbose
            )

            # ---- Validate structure ----
            if not function_call_result.parts:
                raise Exception("Function call result has no parts")

            function_response = function_call_result.parts[0].function_response
            if function_response is None:
                raise Exception("Missing function_response")

            if function_response.response is None:
                raise Exception("Missing function response content")

            function_responses.append(function_call_result.parts[0])

            # ---- Print tool output immediately ----
            result_data = function_response.response

            if args.verbose:
                print(f"-> {result_data}")

            if isinstance(result_data, dict):
                if "result" in result_data:
                    print(result_data["result"])
                elif "error" in result_data:
                    print(result_data["error"])

        # ---- Give tool outputs back to model ----
        messages.append(
            types.Content(role="user", parts=function_responses)
        )

        continue

    # ---- Final response from model ----
    else:
        print("\nFinal response:")
        print(response.text)
        break

# ---- Safety stop ----
else:
    print("Agent stopped: maximum iterations reached.")
    exit(1)

