from app.ml.generate import generate_story
from app.ml.utils import format_prompt

def generate_story_service(request):
    prompt = request.prompt
    genre = request.genre if request.genre else "general"
    formatted_prompt = format_prompt(prompt, genre)

    story_text = generate_story(formatted_prompt)
    return {"story": story_text}
