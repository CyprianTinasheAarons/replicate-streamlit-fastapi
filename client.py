import requests
import streamlit as st


def generate_image(prompt: str) -> str:
    response = requests.post("http://localhost:8000/generate", json={"prompt": prompt})
    return response.json()["url"]


def main():
    st.title("Flux 1.1 Pro Image Generator")
    prompt = st.text_input("Enter a prompt for the image")
    if st.button("Generate Image"):
        if prompt:
            url = generate_image(prompt)
            st.image(url)
        else:
            st.error("Please enter a prompt")


if __name__ == "__main__":
    main()
    




