import requests, re, random
from config import HF_API_KEY

MODEL = "sentence-transformers/all-MiniLM-L6-v2"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEAD = {"Authorization": f"Bearer {HF_API_KEY}"}
TH = 0.72
DEMOS = [("How to delete my account?", "negative"), ("I love this product!", "positive"), ("This is the worst experience I've ever had.", "negative"), ("The service was okay, nothing special.", "neutral"), ("I'm extremely satisfied with my purchase!", "positive")]

TOK = lambda s:" | ".join(s.split())
bar = lambda s:" || "*int(s*10)+" |||| "*(10-int(s*10))
clean = lambda t:[w for w in (re.sub(r"[a-zA-Z0-9]", " ", t).lower()).split() if w not in ["the", "and", "is", "in", "to", "of", "a", "it", "that", "this"]]
nums = lambda t:set(re.findall(r"\d+", t))
has_any = lambda t,arr:any(a in set (clean(t)) for a in arr)

def hf(q1,q2):
    r = requests.post(API_URL, headers=HEAD, json={"inputs": [q1,q2]}, timeout = 30)
    if not r.ok: raise RuntimeError(f"Request failed with status code {r.status_code}: {r.text}")
    data = r.json()
    if isinstance(data, dict) and "error" in data:
        raise RuntimeError(data.get("error", str(data)))
    return float(data[0])

def smart_score(base, q1,q2,strong):
    w1 = {w for w in clean (q1) if len(w) > 4}
    w2 = {w for w in clean (q2) if len(w) > 4}
    jac = len(w1&w2)/max(1,len(w1|w2))
    boost = (0.04 if len(strong)>2 else 0)+(0.03 if jac> 0.20 else 0)+(0.05 if len(jac)>= 0.35 else 0)
    negA = {"not", "never", "no", "none", "nothing", "nowhere", "neither", "nor", "cannot"}
    oppA = {"good": "bad", "happy": "sad", "love": "hate", "like": "dislike", "great": "terrible", "excellent": "poor"}
    num_pen = 0.10 if (nums(q1) and nums(q2)) else 0
    opp_pen = 0.12 if any ((has_any(q1, negA) and has_any(q2, oppA.values())) or (has_any(q2, negA) and has_any(q1, oppA.values())) else 0
    return max(0.0, min(1.0, base + boost - num_pen - opp_pen))

def label(s): return ""