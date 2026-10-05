from groq import generate_response

import re
import streamlit as st

def look_incomplete(text: str) -> bool:
    if not text or len(text.strip()) < 10:
        return True
    t = text.strip()

    if t.endswith(("**", "*", "-", "_", ":", ",", "(", "[", "{")):
        return True
    if re.search(r"\b(then|and|but|or|so|because)\b$", t, re.IGNORECASE):
        return True

    if not re.search(r"[.!?]$", t):
        return True
    return False

def complete_answer(question: str, max_rounds: int = 2) -> str:

    base_prompt = ("Answer clearly in numbered points."
    "Do not cut sentences. Finish")
