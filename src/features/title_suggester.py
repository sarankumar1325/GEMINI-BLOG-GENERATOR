import openai

def suggest_titles(topic):
    try:
        response = openai.Completion.create(
            model='gpt-4.1',
            prompt=f"Suggest catchy titles for a blog post about: {topic}",
            max_tokens=60,
            temperature=0.7
        )
        titles = response.choices[0].text.strip().split('\n')
        return titles
    except Exception as e:
        return [f"Error: {e}"]