
from io import BytesIO
import os
import requests
import streamlit as st
from groq import Groq

# ---------------- CONFIGURATION ----------------

GROQ_MODEL = "llama-3.3-70b-versatile"
FILTER_API_URL = "https://filters-zeta.vercel.app/api/filter"

ENHANCE_SYS = (
    "Improve prompts for text-to-image. Return ONLY the enhanced prompt. "
    "Add subject, style, lighting, camera angle, background, colors. "
    "Keep it safe."
)

GROQ_API_KEY = (
    os.getenv("GROQ_API_KEY")
    or st.secrets.get("GROQ_API_KEY", "")
)


# ---------------- SAFETY FILTER ----------------

def check_prompt_with_filter_api(prompt: str):
    try:
        response = requests.post(
            FILTER_API_URL,
            json={"prompt": prompt},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            return {
                "ok": False,
                "reason": "Invalid filter API response.",
            }

        return data

    except (requests.RequestException, ValueError) as e:
        return {
            "ok": False,
            "reason": f"Filter API error: {e}",
        }


# ---------------- GROQ PROMPT ENHANCEMENT ----------------

def enhance_prompt(raw: str) -> str:
    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": ENHANCE_SYS},
            {"role": "user", "content": raw},
        ],
        temperature=0.4,
        max_completion_tokens=220,
    )

    result = response.choices[0].message.content
    return result.strip() if result and result.strip() else raw


# ---------------- IMAGE GENERATION ----------------

def gen_image(prompt: str):
    # Keep the safety check before image generation.
    filter_result = check_prompt_with_filter_api(prompt)

    if not filter_result.get("ok"):
        return None, (
            "⚠️ Prompt blocked by safety filter. "
            + filter_result.get("reason", "Unsafe prompt")
        )

    # Groq's standard chat API does not generate images.
    # Connect your chosen image-generation API here.
    return None, (
        "Image generation is not configured. Groq enhances "
        "the prompt, but an image-generation API is required "
        "to create the image."
    )


# ---------------- MAIN APP ----------------

def main():
    st.set_page_config(
        page_title="Safe AI Image Generator",
        layout="centered",
    )

    st.title("🖼️ Safe AI Image Generator")
    st.info(
        "Enter a prompt → enhance it with Groq → check safety "
        "→ generate an image using an image-generation provider."
    )

    if not GROQ_API_KEY:
        st.error(
            "Groq API key missing. Add GROQ_API_KEY to "
            ".streamlit/secrets.toml."
        )
        st.stop()

    with st.form("image_form"):
        raw = st.text_area(
            "Image Description",
            height=120,
            placeholder=(
                "Example: A cozy cabin in snowy mountains "
                "at sunrise, cinematic lighting"
            ),
        )
        submit = st.form_submit_button("Generate Image")

    if submit:
        raw = raw.strip()

        if not raw:
            st.warning("⚠️ Please enter an image description.")
            return

        # Check original prompt.
        with st.spinner("Checking original prompt..."):
            raw_check = check_prompt_with_filter_api(raw)

        if not raw_check.get("ok"):
            st.error(
                "⚠️ Prompt blocked or filter unavailable. "
                + raw_check.get("reason", "Unsafe prompt")
            )
            return

        # Enhance with Groq.
        try:
            with st.spinner("Enhancing prompt with Groq..."):
                final_prompt = enhance_prompt(raw)
        except Exception as e:
            st.error(f"Groq API error: {e}")
            return

        # Check enhanced prompt.
        enhanced_check = check_prompt_with_filter_api(final_prompt)

        if not enhanced_check.get("ok"):
            st.error(
                "⚠️ Enhanced prompt blocked or filter unavailable. "
                + enhanced_check.get("reason", "Unsafe prompt")
            )
            return

        st.markdown("#### Enhanced Prompt")
        st.code(final_prompt)

        with st.spinner("Generating image..."):
            img, err = gen_image(final_prompt)

        if err:
            st.error(err)
            return

        st.image(
            img,
            caption="Generated Image",
            use_container_width=True,
        )
        st.session_state.generated_image = img

    img = st.session_state.get("generated_image")

    if img is not None:
        buf = BytesIO()
        img.save(buf, format="PNG")

        st.download_button(
            "📥 Download Image",
            buf.getvalue(),
            "ai_generated_image.png",
            "image/png",
        )


if __name__ == "__main__":
    main()
