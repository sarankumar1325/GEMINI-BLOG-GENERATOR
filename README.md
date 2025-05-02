# Gemini Blog Generator

## Overview
Gemini Blog Generator is a web application that leverages Google Gemini's powerful language model to help you generate blog content, outlines, catchy titles, and summaries. The app features an interactive, Streamlit-like interface for a seamless user experience.

## Features
- **Blog Content Generation:** Generate paragraphs or full blog posts based on your topic.
- **Outline Generator:** Create structured outlines for your blog posts.
- **Title Suggester:** Get catchy and relevant blog post titles.
- **Summary Generator:** Summarize existing blog content or articles.
- **Modern Web UI:** Built with Streamlit (or similar), providing an easy-to-use, interactive interface.

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
pip install streamlit google-generativeai
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
│   ├── app.py                # Main Streamlit app
│   ├── features/             # Feature modules (outline, title, summary, etc.)
│   └── utils/                # Utility functions
├── requirements.txt          # Python dependencies
├── .env                      # Gemini API key
└── README.md                 # Project documentation
```

## Notes
- This project uses Google Gemini for all text generation tasks.
- Make sure your API key is kept private and not shared publicly.

## License
MIT License