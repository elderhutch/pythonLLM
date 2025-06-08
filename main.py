import os
from dotenv import load_dotenv
from google import genai
import sys

if len(sys.argv) < 2:
    sys.stderr.write("Error: No input provided.\n")
    sys.exit(1)
prompt = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

model = "gemini-2.0-flash-001"
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

gen_ai_response = client.models.generate_content(model=model, contents=prompt)
print(gen_ai_response.text)
print("Prompt tokens:", gen_ai_response.usage_metadata.prompt_token_count)
print("Response tokens:")