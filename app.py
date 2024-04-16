from openai import OpenAI
import streamlit as st

# Load API key from a file
with open("keys/key_01.txt", "r") as f:
    api_key = f.read().strip()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def generate_code(prompt_text):
    # Generate code completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a helpful AI Assistant and Code reviewer
            Find the Bugs and error in the program."""},
            {"role": "user", "content": prompt_text}
        ]
    )
    return response.choices[0].message.content

# Streamlit web app
def main():
    st.title("Code Debugging Tool💬🤖")
    st.subheader("Write your program📝")
    prompt = st.text_area("Enter the code...")
    if st.button("Generate"):
        corrected_code = generate_code(prompt)
        st.write(corrected_code)

if __name__ == "__main__":
    main()
