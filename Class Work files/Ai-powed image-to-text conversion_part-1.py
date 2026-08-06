import requests, base64, os, re, time
from PIL import Image
from colorama import Fore, Style, init

init(autoreset=True)

ROUTER_URL = ""
HEADERS = {"Authorization": f"Bearer API_KEY", "Content-Type": "application/json"}

VISION_MODELS = [

"moonshotai/Kimi-K2.6:novita",

"meta-llama/Llama-4-Maverick-17B-128E-Instruct:sambanova",

"meta-llama/Llama-3.2-11B-Vision-Instruct:sambanova",

]

TEXT_MODELS = [

"Qwen/Qwen2.5-7B-Instruct:together",

"Qwen/Qwen2.5-14B-Instruct:together",

"Qwen/Qwen2.5-32B-Instruct:together",

"mistralai/Mistral-7B-Instruct-v0.3:together",

"mistralai/Mixtral-8x7B-Instruct-v0.1:together",

]

def _data_url(path: str) -> str:
    with open(path, "rb") as f:
        return "data:image/jpg;base64, "+ base64.b64encode(f.read()).decode("utf-8")

def query_hf_api(payload: dict):
    try:
        r = requests.post(ROUTER_URL, headers=HEADERS, json=payload, timeout=120)
    except requests.RequestException as e:
        print(Fore.RED + f"Request failed: {e}")
        return None
    if r.status_code != 200:
        try:
            j = r.json()
            msg = j.get("error", {}).get("message") or str(j)
        except Exception as e:
            msg = f"Error parsing JSON response: {e}"
        print(Fore.RED + f"API Error: {msg}")
        return None
    try:
        return r.json(), None
    except Exception:
        return None, "Non-Json respones receivd from the API."

def _extract_text(data) -> str:
    msg = (data or {}).get("Choices", [{}])[0].get("Message", {}) or {}
    return (msg.get("content") or "").strip()

def _run_models(models, messages, max_tokens = 160, temperature = 0.3):
    for model in models

