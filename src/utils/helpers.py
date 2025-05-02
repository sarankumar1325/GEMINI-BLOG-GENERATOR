def validate_topic(topic):
    if not topic or len(topic) < 3:
        raise ValueError("Topic must be at least 3 characters long.")
    return topic

def format_paragraph(paragraph):
    return paragraph.strip().capitalize()

def handle_api_error(error):
    if hasattr(error, 'http_status'):
        return f"API Error: {error.http_status} - {error.user_message}"
    return "An unexpected error occurred while communicating with the API."