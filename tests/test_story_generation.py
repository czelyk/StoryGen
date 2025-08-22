import pytest
from app.ml.generate import generate_story

def test_generate_story_basic():
    prompt = "Genre: fantasy. Story: A brave knight embarks on a quest."
    story = generate_story(prompt, max_length=100)
    assert isinstance(story, str)
    assert len(story) > 0
    assert "knight" in story.lower()
