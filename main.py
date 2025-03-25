import streamlit as st
from openai import OpenAI
from ui import get_character_inputs
from prompts import generate_prompt

st.set_page_config(page_title="D&D Character Backstory Generator")
st.title("🧙 D&D Character Backstory Generator")

# API key input in sidebar
user_api_key = st.sidebar.text_input("API Key (OpenRouter)", type="password")

# Generator function
def generate_response(input_text):
    status_message = st.empty()
    status_message.info("Generating...")

    try:
        # Initialize OpenAI client with OpenRouter
        client = OpenAI(
            api_key=user_api_key,
            base_url="https://openrouter.ai/api/v1",
        )

        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat",  # you can change to "gpt-4" or another model if needed
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in creating deep, immersive, and emotionally rich Dungeons & Dragons character backstories. Generate a compelling backstory, three adventure hooks, and an Adobe Firefly art prompt for the following character.",
                },
                {"role": "user", "content": input_text},
            ],
        )

        output = completion.choices[0].message.content
        clean_output = output.split(r"\boxed{")[0].strip()
        st.markdown(clean_output)
        status_message.empty()

    except Exception as e:
        status_message.empty()
        st.error(f"An error occurred: {e}")

# Form for character input
with st.form("my_form"):
    user_data = get_character_inputs()
    submitted = st.form_submit_button("🪄 Generate Backstory")

if submitted:
    if not user_api_key:
        st.warning("Please enter an API key.")
    elif not user_api_key.startswith("sk-"):
        st.warning("Please enter a valid API key starting with 'sk-'.")
    else:
        prompt = generate_prompt(user_data)
        generate_response(prompt)
