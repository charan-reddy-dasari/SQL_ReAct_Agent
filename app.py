
import streamlit as st
import logging

from agent import initialize_agent, ask_agent

logging.basicConfig(level=logging.ERROR)

st.set_page_config(
    page_title="SQL AI Agent",
    page_icon="🤖"
)

st.title("🤖 SQL AI Agent")
st.caption("Ask questions about your database.")

# Initialize agent
@st.cache_resource
def get_agent():
    return initialize_agent()


try:
    agent = get_agent()

except Exception:
    logging.exception("Agent initialization failed")
    st.error(
        "Unable to initialize SQL Agent. "
        "Check your API key and database connection."
    )
    st.stop()


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Clear chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
question = st.chat_input("Ask a question about your database...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        try:
            with st.spinner("Analyzing database..."):

                answer = ask_agent(agent, question)

            st.markdown(answer)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception:
            logging.exception("Question processing failed")

            st.error(
                "Something went wrong while processing your question. "
                "Please try again."
            )
