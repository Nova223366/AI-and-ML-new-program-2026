from groq import generate_response

import streamlit as st
import io

def role_prompt(role: str, q: str) -> str:
    if role == "Teacher":
        return f"You are a teacher. Explain clearly with simple words and 3-5 bullet points.\nQuestion: {q}"
    if role == "Expert":
        return f"You are an expert. Give a detailed, technical explanation with examples.\nQuestion: {q}"
    return f"You are a friendly helper. Answer warmly and simply with a short example.\nQuestion: {q}"

def setup_ui():
    st.title("Enhanced AI Teaching Assistant")
    st.write("Ask questions and get AI responses tailored by role. Your conversation history is saved below!")

    st.session_state.setdefault("conversation", [])

    role = st.selectbox("Select AI Role", ["Teacher", "Expert", "Friendly Helper"])
    user_input = st.text_input("Enter your question here:", placeholder="Example: What is photosynthesis?")

    c1, c2 = st.columns([1, 1])
    with c1:
        ask = st.button("Ask")
    with c2:
        clear = st.button("Clear Conversation")

    if ask:
        if user_input.strip():
            prompt = role_prompt(role, user_input.strip())
            with st.spinner("Generating response..."):
                answer = generate_response(prompt, temperature=0.3, max_tokens=1024)
            st.session_state.conversation.append({"role": role, "question": user_input.strip(), "answer": answer})
            st.rerun()
        else:
            st.warning("⚠️ Please enter a question before clicking Ask.")

    if clear:
        st.session_state.conversation = []
        st.rerun()

    if st.session_state.conversation:
        # Export
        export_text = ""
        for i, chat in enumerate(st.session_state.conversation, 1):
            export_text += f"Q{i} ({chat['role']}): {chat['question']}\nA{i}: {chat['answer']}\n\n"
        st.download_button(
            "📄 Export Chat History",
            io.BytesIO(export_text.encode("utf-8")),
            "Enhanced_AI_Teaching_Assistant_Conversation.txt",
            "text/plain",
        )

        st.markdown("### Conversation History")
        for i, chat in enumerate(st.session_state.conversation, 1):
            st.markdown(f"**You:** {chat['question']}")
            st.markdown(f"**AI ({chat['role']}):** {chat['answer']}")
            st.markdown("---")

def main():
    setup_ui()

if __name__ == "__main__":
    main()
