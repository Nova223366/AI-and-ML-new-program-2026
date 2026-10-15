from Groq import generate_respones

import io, streamlit as st

SYSTEM_PROMPT = """ You are a Mastermind. For every math problem: 
1) Show step-by-step solution
2) Explain reasoning
3) Give alternative method if possible
4) Verify answer if possible 
5) Use proper notation
6) Break complex problems into parts

Format: Problem -> Step -> **Final Answer** -> Concepts used. Be precise and educational.
"""

def math_generate(problems: str, level: str, temperature=0.1, max_tokens=1024) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nMAth Problem ({level}): {problems}" 
    return generate_respones(prompt, temperature=temperature, max_tokens=max_tokens)

def expert_txt(history):
    txt = "\n\n".join([f"Q{i}: {h['q']}\nA{i}: {h['a']} for i, h in"])