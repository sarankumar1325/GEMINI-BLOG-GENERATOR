import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load Gemini API key from .env
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(env_path)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    GEMINI_API_KEY = "YOUR_API_KEY"

def gemini_generate(prompt, model="gemini-2.0-flash"):
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]
        generate_content_config = types.GenerateContentConfig(
            response_mime_type="text/plain",
        )
        result = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            result += chunk.text
        return result.strip()
    except Exception as e:
        return f"Error: {e}"

st.set_page_config(page_title="Gemini Blog Generator", layout="centered")
st.title("📝 Gemini Blog Generator")

menu = st.sidebar.radio("Choose a feature:", (
    "Generate Blog Paragraph",
    "Generate Outline",
    "Suggest Titles",
    "Summarize Content"
))

if menu == "Generate Blog Paragraph":
    topic = st.text_input("Enter the topic for your blog paragraph:")
    if st.button("Generate Paragraph") and topic:
        prompt = f"Write a detailed blog paragraph about: {topic}"
        result = gemini_generate(prompt)
        st.text_area("Generated Paragraph", value=result, height=200)
        if st.button("Save to File"):
            with open("generated_blog.txt", "a", encoding="utf-8") as f:
                f.write(result + "\n\n")
            st.success("Content saved to generated_blog.txt")

elif menu == "Generate Outline":
    topic = st.text_input("Enter the topic for your blog outline:")
    if st.button("Generate Outline") and topic:
        prompt = f"Generate a structured outline for a blog post about: {topic}"
        result = gemini_generate(prompt)
        st.text_area("Generated Outline", value=result, height=200)
        if st.button("Save to File"):
            with open("generated_blog.txt", "a", encoding="utf-8") as f:
                f.write(result + "\n\n")
            st.success("Content saved to generated_blog.txt")

elif menu == "Suggest Titles":
    topic = st.text_input("Enter the topic for title suggestions:")
    if st.button("Suggest Titles") and topic:
        prompt = f"Suggest 5 catchy titles for a blog post about: {topic}"
        result = gemini_generate(prompt)
        st.text_area("Suggested Titles", value=result, height=120)
        if st.button("Save to File"):
            with open("generated_blog.txt", "a", encoding="utf-8") as f:
                f.write(result + "\n\n")
            st.success("Content saved to generated_blog.txt")

elif menu == "Summarize Content":
    content = st.text_area("Paste the content you want to summarize:")
    if st.button("Summarize") and content:
        prompt = f"Summarize the following content:\n{content}"
        result = gemini_generate(prompt)
        st.text_area("Summary", value=result, height=120)
        if st.button("Save to File"):
            with open("generated_blog.txt", "a", encoding="utf-8") as f:
                f.write(result + "\n\n")
            st.success("Content saved to generated_blog.txt")
