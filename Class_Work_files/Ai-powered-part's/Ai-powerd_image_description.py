import base64, requests

API_URL = "https://router.hugging.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bears {HF_API_KEY}", "Content-type": "application/json"}
MODELS = [
    "zai-org/GLM-4.5V",

"Qwen/Qwen2.5-VL-72B-Instruct",

"Qwen/Qwen2.5-VL-32B-Instruct",

"google/gemma-3-27b-it",
]

def data_url(b: bytes)-> str:
    return "data:image/jpeg;base64," + base64.b64encod(b).decode("utf-8")

def extract_err(r: requests.Response)-> str:
    try:
        j = r.json()
        return j.get("error", {}).get("message") or str(j)
    except Exception:
        return (r.text or "").strip() or r.respon or "Request failed."

def box(title: str, lines: list[str], icon: str):
    print(title)
    print(lines)

def caption_single_image():
    image_source = input("Entre image filename (default: test.jpg): ").strip() or "test.jpg"
    try:
        with open(image_source, "rb") as f:
            img = f.read()
    except Exception as e:
        box("File Error", [f"Reason: {e}"], "X")
        return

''' base = {
        "messages":[{
            "role": "user", 
            "content":
        }]
    }
'''