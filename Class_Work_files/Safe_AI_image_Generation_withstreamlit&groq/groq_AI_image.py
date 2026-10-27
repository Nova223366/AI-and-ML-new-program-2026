
import os
from groq import Groq

GROQ_MODEL = "llama-3.3-70b-versatile"

ENHANCE_SYS = """
You are an expert text-to-image prompt engineer.

Enhance the user's image description by adding:
- Subject details
- Artistic style
- Lighting
- Camera angle
- Background and environment
- Color palette
- Textures and composition

Return ONLY the enhanced image prompt.
Do not include explanations, headings, or quotation marks.
Keep the prompt safe and suitable for image generation.
"""


def generate_response(
    prompt: str,
    temperature: float = 0.4,
    max_tokens: int = 220,
) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Set it as an environment variable."
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": ENHANCE_SYS,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens,
    )

    result = response.choices[0].message.content

    if not result or not result.strip():
        raise ValueError("Groq returned an empty response.")

    return result.strip()
