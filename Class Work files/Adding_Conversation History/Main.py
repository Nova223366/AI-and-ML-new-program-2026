from groq import generate_response

import io
import streamlit as st

CSS = """
<style>
.history-wrap {max-height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;}

.qa-card{border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; border-radius: 5px;}

.q{font-weight: 700; color: #333; margin-bottom: 5px;}

.a{white-space: pre-wrap; color: #555; line-height: 1.5; margin-bottom: 5px;}
</style>
"""

def export_bytes(history):
    text = "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1)])
    return io.BytesIO(text.encode("utf-8"))

#simple chat history saver
def setup_ui():
    st.set_page_config(page_title="Chat with Groq", page_icon="🤖", layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state.history = []

    st.title("Chat with Groq")
    st.write("Ask questions and get answers from the Groq model.")

    with st.form(key="chat_form"):
        user_input = st.text_area("Your question:", height=100)
        submit_button = st.form_submit_button(label="Send")

    if submit_button and user_input.strip():
        answer = generate_response(user_input)
        st.session_state.history.append({"question": user_input, "answer": answer})
        user_input = ""  # Clear input after submission

    if st.session_state.history:
        with st.expander("Conversation History", expanded=True):
            for i, h in enumerate(st.session_state.history, 1):
                st.markdown(f'<div class="qa-card"><div class="q">Q{i}: {h["question"]}</div><div class="a">A{i}: {h["answer"]}</div></div>', unsafe_allow_html=True)

        export_button = st.download_button(
            label="Export Conversation History",
            data=export_bytes(st.session_state.history),
            file_name="conversation_history.txt",
            mime="text/plain"
        )

        cards = []
        for i, h in enumerate(st.session_state.history, 1):
            cards.append(f'<div class="qa-card"><div class="q">Q{i}: {h["question"]}</div><div class="a">A{i}: {h["answer"]}</div></div>')
        st.markdown('<div class="history-wrap">' + ''.join(cards) + '</div>', unsafe_allow_html=True)

def main():
    setup_ui()

if __name__ == "__main__":
    main()
