import openai

def summarize_blog(content):
    try:
        response = openai.Completion.create(
            model='gpt-4.1',
            prompt='Summarize the following content:\n' + content,
            max_tokens=150,
            temperature=0.5
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        return f"Error: {e}"