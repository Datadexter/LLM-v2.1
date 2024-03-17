import streamlit as st
import google.generativeai as allm
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.environ.get("API_KEY")
allm.configure(api_key=API_KEY)

def main():
    st.header("Chat with A-LLM")
    st.write("")

    prompt = st.text_input("Prompt please...", placeholder="Prompt", label_visibility="visible")
    temp = st.slider("Temperature", 0.0, 1.0, step=0.05)    #Hyper parameter - range[0-1]

    if st.button("SEND", use_container_width=True):
        model = "models/text-bison-001"    #This is the only model currently available

        response = allm.generate_text(
            model=model,
            prompt=prompt,
            temperature=temp,
            max_output_tokens=1024
        )

        st.write("")
        st.header(":blue[Response]")
        st.write("")

        st.markdown(response.result, unsafe_allow_html=False, help=None)

if __name__ == "__main__":
    main()
