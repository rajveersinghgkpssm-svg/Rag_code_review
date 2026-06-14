import google.generativeai as genai

genai.configure(
api_key="YOUR_API_KEY"
)

model=genai.GenerativeModel(
"gemini-1.5-pro"
)


def ask_gemini(
query,
context
):

    prompt=f"""
Context:

{context}

Question:
{query}

Provide:
•⁠  ⁠Review
•⁠  ⁠Errors
•⁠  ⁠Improvements
"""

    res=model.generate_content(
        prompt
    )

    return res.text