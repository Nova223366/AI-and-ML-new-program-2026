# groq.py

from openai import OpenAI
import config


GROQ_URL = "https://api.groq.com/openai/v1"


def get_client():
    """Create and return the Groq OpenAI-compatible client."""

    api_key = getattr(config, "GROQ_API_KEY", None)

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is missing from config.py"
        )

    return OpenAI(
        api_key=api_key,
        base_url=GROQ_URL,
    )


def list_models():
    """
    Ask Groq which models are available to this API key.
    Useful for debugging model_not_found errors.
    """

    try:
        client = get_client()

        models = client.models.list()

        print("\n========== AVAILABLE GROQ MODELS ==========")

        for model in models.data:
            print(model.id)

        print("===========================================\n")

        return [model.id for model in models.data]

    except Exception as e:
        print("\n========== MODEL LIST ERROR ==========")
        print(type(e).__name__)
        print(e)
        print("======================================\n")

        return []


def generate_response(
    prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 512,
) -> str:

    try:
        client = get_client()

    except Exception as e:
        return (
            "Groq client error:\n"
            f"{type(e).__name__}: {e}"
        )

    models = getattr(
        config,
        "GROQ_MODELS",
        ["openai/gpt-oss-20b"],
    )

    errors = []

    for model in models:

        print(f"[DEBUG] Trying model: {model}")

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

            if not response.choices:
                raise RuntimeError(
                    "Groq returned no choices."
                )

            content = response.choices[0].message.content

            if not content:
                raise RuntimeError(
                    "Groq returned empty content."
                )

            print(
                f"[DEBUG] Model succeeded: {model}"
            )

            return content.strip()

        except Exception as e:

            print(
                f"[DEBUG] Model failed: {model}"
            )

            print(
                f"[DEBUG] Error: "
                f"{type(e).__name__}: {e}"
            )

            errors.append(
                f"{model}: "
                f"{type(e).__name__}: {e}"
            )

    return (
        "\nGroq request failed.\n\n"
        f"Models tried: {models}\n\n"
        "Errors:\n"
        + "\n".join(errors)
    )
