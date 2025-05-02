# Gemini Blog Generator
![Image](https://github.com/user-attachments/assets/0d217c9f-bec3-4f6f-9d6d-67a77149a46e)
## Overview
Gemini Blog Generator is a web application that leverages Google Gemini's powerful language model to help you generate blog content, outlines, catchy titles, and summaries. The app features an interactive, Streamlit-based interface for a seamless user experience.

## Features
- **Blog Content Generation:** Generate paragraphs or full blog posts based on your topic.
- **Outline Generator:** Create structured outlines for your blog posts.
- **Title Suggester:** Get catchy and relevant blog post titles.
- **Summary Generator:** Summarize existing blog content or articles.
- **Modern Web UI:** Built with Streamlit, providing an easy-to-use, interactive interface.
- **Save to File:** Save generated content to a local text file.

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repository-url>
cd openai-blog-generator
```

### 2. Create a Virtual Environment (Recommended)
```sh
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
pip install streamlit google-genai python-dotenv
```

### 4. Configure Gemini API Key
Create a `.env` file in the project root with the following content:
```
GEMINI_API_KEY=AIzaSyDeUr2NKIh3J1elan_EZBxgeNQC-hTiF_E
```

### 5. Run the Application
```sh
streamlit run src/app.py
```

## Usage
- Open your browser to the provided local URL (usually http://localhost:8501).
- Use the sidebar to select features: generate content, outlines, titles, or summaries.
- Enter your topic or content and let Gemini do the rest!
- Optionally, save generated content to a file.

## Project Structure
```
openai-blog-generator/
├── src/
│   ├── app.py                # Main Streamlit app (Gemini-powered)
│   ├── blog_generator.py     # (Legacy) OpenAI CLI version
│   ├── features/             # Feature modules (outline, title, summary, etc.)
│   └── utils/                # Utility functions
├── requirements.txt          # Python dependencies
├── .env                      # Gemini API key
└── README.md                 # Project documentation
```

## Notes
- This project uses Google Gemini for all text generation tasks in the Streamlit app.
- The legacy CLI version (blog_generator.py) uses OpenAI and is not maintained.
- Make sure your API key is kept private and not shared publicly.

## Troubleshooting
- If you see `ImportError: cannot import name 'genai' from 'google'`, ensure you have no local folder named `google` and that you have installed `google-genai`.
- If you see model errors, ensure you are using the correct model name (e.g., `gemini-2.0-flash`).

