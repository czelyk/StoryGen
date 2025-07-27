import re

def clean_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # Çoklu boşlukları tek boşluğa indirger
    text = re.sub(r'\n+', '\n', text)  # Çoklu satır boşluklarını tek satıra indirger
    return text

def format_prompt(prompt: str, genre: str) -> str:
    prompt = clean_text(prompt)
    genre = clean_text(genre)
    return f"Genre: {genre}. Story: {prompt}"
