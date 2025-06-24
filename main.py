import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1] if len(sys.argv) > 1 else print("No Prompt entered, exitting")
flag = sys.argv[2] if len(sys.argv) > 2 else None
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

if flag == '--verbose':
    print(f'User prompt: {user_prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}')
else:
    print(f'Response :{response}')
