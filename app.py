import streamlit as st
import google.generativeai as genai

# 1. Page ki settings
st.set_page_config(page_title="Mera ChatGPT", page_icon="🤖")
st.title("Mera Apna ChatGPT 🤖")

# 2. API Key (Yahan apni sahi key check karein)
# Tip: Key ke shuru ya aakhir mein koi khali jagah (space) nahi honi chahiye
API_KEY = "AIzaSyBH6KJA5V66tCNm3VbZGdCYE26xgYlNOfs"

try:
    genai.configure(api_key=API_KEY)
    # 1.5-flash sabse naya aur fast hai
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Setup mein masla hai: {e}")

# 3. Chat history save karne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani baatein dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Naya sawal puchna
if prompt := st.chat_input("Kuch puchein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # AI se jawab mangna
        response = model.generate_content(prompt)
        full_response = response.text
        
        with st.chat_message("assistant"):
            st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    except Exception as e:
        st.error("Google AI ne jawab nahi diya. Shayad API Key expire ho gayi hai ya internet slow hai.")
        st.info("Mashwara: Ek nayi API Key bana kar check karein.")
