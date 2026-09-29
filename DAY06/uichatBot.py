import ollama
import streamlit as st
st.subheader("👾welcome to my personal chatBot Assitant!!!")
with st.sidebar:
    st.markdown(
    "<h3 style='font-style:italic; font-family:cursive;'>✨ Choose Your Assistant</h3>",
    unsafe_allow_html=True
)
    category = st.selectbox(
        "Select a category",
        [
            "🎓 Study",
            "😂 Fun",
            "💻 Coding",
            "📝 Writing",
            "💡 Ideas", 
            "📚 General",
            "❤️ Personal"
        ]
    )
personalities = {
    "🎓 Study": "You are a study assistant. Explain concepts simply with examples.",
    "😂 Fun": "You are a fun and friendly assistant. Make conversations interesting and entertaining.",
    "💻 Coding": "You are a coding assistant. Give simple code and explain it clearly.",
    "📝 Writing": "You are a writing assistant. Help with writing, grammar and content.",
    "💡 Ideas": "You are a creative assistant. Give useful and creative ideas.",
    "📚 General": "You are a helpful general personal assistant.",
    "❤️ Personal": "You are a friendly personal assistant. Give supportive and practical answers."
}
with st.sidebar:
    st.header(":blue[Chat settings]")
    if st.button("Clear Chat 🗑️"):
        st.session_state.messages = []
        st.success("chat cleared👍")
    personalities = {
        "kid": "Answer the questions like you are explaining to a 5 year old kid. Give answer in two lines only",
        "Friend": "Answer the questions in friendly and casual manner. Give answer in two lines only",
        "professor": "Answer the questions like a professor. Give clear and detailed answers"
    }
    personality = st.selectbox("select a personality", personalities.keys())
    uploaded_file = st.file_uploader("📁upload a text file...")
    try:
        if uploaded_file:
            st.success("File uploaded successfully👍")
            context = uploaded_file.read().decode("utf-8")
            if st.button("Display"):
                st.text(context)
    except:
        st.error("File type not supported")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("💭Ask me anything: ")
if question:
    st.session_state.messages.append(
        {"role": "user",
         "content": question}
    )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("AI is thinking🧠...."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {"role": "system", "content": personalities[personality]}
            ] + st.session_state.messages
        )
    st.session_state.messages.append(
        {"role": "assistant",
         "content": response["message"]["content"]}
    )
    with st.chat_message("Assistant"):
        st.write("AI:", response["message"]["content"])