import config
from openai import OpenAI

GROQ_URL = "https://api.groq.com/openai/v1"

# Use currently supported Groq models.
MODELS = getattr(
    config,
    "GROQ_MODELS",
    [
        "openai/gpt-oss-20b",
        "openai/gpt-oss-120b",
    ],
)


def generate_response(
    prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 512,
) -> str:
    key = getattr(config, "GROQ_API_KEY", None)

    if not key:
        return "Error: GROQ_API_KEY missing in config.py"

    client = OpenAI(
        api_key=key,
        base_url=GROQ_URL,
    )

    last_err = None

    for model in MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )

            answer = response.choices[0].message.content
            return answer or "The AI returned an empty response."

        except Exception as error:
            last_err = error

    return (
        "Groq model failed.\n"
        f"Tried models: {MODELS}\n"
        f"Details: {type(last_err).__name__}: {last_err}\n"
        "Check your API key, model availability, and network connection."
    )