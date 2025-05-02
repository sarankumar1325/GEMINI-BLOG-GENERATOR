# Generate a Blog with OpenAI 📝

import openai
from dotenv import dotenv_values
from features.outline_generator import generate_outline
from features.title_suggester import suggest_titles
from features.summary_generator import summarize_blog
from utils.helpers import validate_topic, handle_api_error

config = dotenv_values('.env')
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    try:
        topic = validate_topic(paragraph_topic)
        response = openai.Completion.create(
            model='gpt-4.1',
            prompt='Write a paragraph about the following topic: ' + topic,
            max_tokens=400,
            temperature=0.3
        )
        retrieve_blog = response.choices[0].text.strip()
        return retrieve_blog
    except Exception as e:
        return handle_api_error(e)

def save_to_file(content, filename="generated_blog.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n\n")
        print(f"Content saved to {filename}")
    except Exception as e:
        print(f"Failed to save file: {e}")

def main():
    keep_writing = True
    while keep_writing:
        print("\nOptions:")
        print("1. Generate a blog paragraph")
        print("2. Generate an outline for a blog post")
        print("3. Suggest catchy titles")
        print("4. Summarize a blog post")
        print("5. Save last generated content to file")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        last_content = None

        if choice == '1':
            paragraph_topic = input('What should this paragraph talk about? ')
            result = generate_blog(paragraph_topic)
            print(result)
            last_content = result
        elif choice == '2':
            outline_topic = input('What topic do you want an outline for? ')
            result = generate_outline(outline_topic)
            print(result)
            last_content = result
        elif choice == '3':
            title_topic = input('What is the topic of your blog post? ')
            result = suggest_titles(title_topic)
            print("\n".join(result) if isinstance(result, list) else result)
            last_content = "\n".join(result) if isinstance(result, list) else result
        elif choice == '4':
            content_to_summarize = input('Paste the content you want to summarize: ')
            result = summarize_blog(content_to_summarize)
            print(result)
            last_content = result
        elif choice == '5':
            if last_content:
                save_to_file(last_content)
            else:
                print("No content to save. Generate something first.")
        elif choice == '6':
            keep_writing = False
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()