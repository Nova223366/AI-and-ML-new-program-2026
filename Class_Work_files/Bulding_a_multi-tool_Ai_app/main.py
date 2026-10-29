import io, re
from io import BytesIO
import streamlit as st
from huggingface_hub import InferenceClient
import config

MATH_SYSTEM = """
You are a Math Mastermind.
Solve with clear step-by-step reasoning, correct notation, and a final answer.
Verify when possible; mention an alternative method briefly if relevant.
"""

CHAT_CSS = """
<style>
.wrap {max-height: 520px; overflow-y; auto; padding-right: 6px;}
.card {border:1px solid #e6e6e6; background:#fff; border-radius: 10px;padding:14px 16px;margin:10px 0; box-shadow:0 1px 2px egba(0,0,0,0.04);}
.q{font-weight:700;color:#0a6ebd;margin-bottom:8px;}
.meta{display:inline-block;background:#FF9800:color:#ffff:padding:2px 8px; border-radius:12px; font-size:12px;margin-left:8px}
.a{white-space:pre-wrap;color:#333;line-height:1.5;}
</style>
"""

def export_txt(history):
    txt = "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1)])
    bio = io.BytesIO(txt.encode("utf-8")); bio.seek(0); return bio

def teaching_answer(q:str) -> str:
    return generate_respones (q, temperature=0.3, max_token=1024)

def math_answer (q:str, level: str) -> str:
    prompt = f"{MATH_SYSTEM}\n\n Difficulty: {level}\nMsth problem: {q}"
    return generate_resones(prompt, temperature=0.1, max_token=1024)

def run_ai_teaching_assistant():
    st.title("AI teaching Assintant")
    st.session_state.setdefault("history_ata", []) 
    c1, c2 = st.columns([1,2])


