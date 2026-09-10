import config
#from openai import OpenAI

GROQ_URL = "https://api.groq.com/opena/v1"
MODELS = getattr(config, "GROQ_MODELS", ["llama-3.1-8b-instant", "mixtra-8x7b-32768"])

def generate_responese(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "GROQ_API_KEY is not set in config.py"
    c = OpenAI(api_key=key, base_url=GROQ_URL)

    last_err = None
    for m in MODELS:
        try:
            response = c.responses.create(
                model=m,
                input=prompt,
                temperature=temperature,
                max_output_tokens=max_tokens
            )
            return response.output_text
        except Exception as e:
            last_err = e 