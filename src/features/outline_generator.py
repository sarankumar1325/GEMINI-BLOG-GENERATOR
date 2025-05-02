import openai

def generate_outline(topic):
    try:
        response = openai.Completion.create(
            model='gpt-4.1',
            prompt=f'Generate a structured outline for a blog post about the following topic: {topic}',
            max_tokens=300,
            temperature=0.5
        )
        outline = response.choices[0].text.strip()
        return outline
    except Exception as e:
        return f"Error: {e}"