import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv(
    "GEMINI_API_KEY"
)

if not api_key:
    raise ValueError(
        "Gemini API key not found"
    )

genai.configure(
    api_key=AQ.Ab8RN6Inob9P_P4SsZ9R5625HmtWdjzo11weQlIHDhzeH_0O6Q
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(
    query,
    context
):

    prompt = f"""
Context:
{context}

Question:
{query}
"""

    response = model.generate_content(
        prompt
    )

    return response.text




print(
os.getenv(
"GEMINI_API_KEY"
))
