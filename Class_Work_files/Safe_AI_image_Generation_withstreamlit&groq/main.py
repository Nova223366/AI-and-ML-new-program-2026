from io import BytesIO
import requests
import streamlit as st
#from

import config

MODEL_ID = "stabilityai/stable-diffusion-3-medium-diffu"
FILTER_API_URL = "https://filters-zeta.vercel.app/api/filter"

ENHANCE_SYS = (
    "Improve prompts for text-to-image. return ONLY the enhance prompt"
    "Add subject, style, lighting, camera angle, background, colors. keep it safe."
)

NEGATIVE = "low quality, blurry, distorted, watermark, text, cropped"

#img_client = InferenceClient(provider="hf-inference", api_key = config.HF_API_KEY)

def check_prompt_with_filter_api(prompt: str):
    try:
        response = requests.post(
            FILTER_API_URL, json={"prompt": prompt}, timeout=10,
            )
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            return {"ok": False, "reason": "Invalid filter API reponse."}

        return data

    except Exception as e:
        return {
            "ok": False, "reason":f"Filter API error: {str(e)}",}

def enhance_prompt(raw: str)-> str:
    from groq_AI_image import generate_respones

    out = generate_respones(
        f"{ENHANCE_SYS}\User prompt: {raw}",
        temperature = 0.4,
        max_token = 220,
    )
    return(out or raw).strip()

def gen_image(prompt: str):
    filter_result = check_prompt_with_filter_api(prompt)
    if not filter_result.get ("ok"):
        return None, f" Prompt blocked by safety filter.{filter_result.get('reason', 'unsafe prompt')}"

    try:
        return img_client.text_to_image(prompt=prompt, negative_)