import streamlit as st
import time

def main():
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "input_key" not in st.session_state:
        st.session_state.input_key = "user_input"

    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**User:** {message['content']}")
        else:
            st.markdown(f"**Bot:** {message['content']}")

    # Input box and send button
    user_input = st.text_input(
        "Type a message...",
        key=st.session_state.input_key,
        placeholder="Type a message..."
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Send"):
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.session_state.user_input = ""
                st.rerun()

    with col2:
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    # Simulate bot response
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        time.sleep(1)
        bot_response = st.session_state.messages[-1]["content"]
        st.session_state.messages.append({"role": "bot", "content": bot_response})
        st.rerun()

if __name__ == "__main__":
    main()