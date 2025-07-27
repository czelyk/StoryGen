from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from functools import lru_cache

app = FastAPI(
    title="AI Story Maker",
    description="Generate creative stories using AI based on your prompt and genre.",
    version="1.0.0"
)

class StoryRequest(BaseModel):
    prompt: str = Field(..., example="A lonely robot explores Mars.")
    genre: Optional[str] = Field("sci-fi", example="sci-fi")

class StoryResponse(BaseModel):
    story: str = Field(..., example="Once upon a time, in a jungle full of mystery...")

# Model yükleme ve tokenizer (cache ile tek seferde)
@lru_cache()
def get_model_and_tokenizer():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return tokenizer, model

def generate_story_text(prompt: str, genre: str) -> str:
    tokenizer, model = get_model_and_tokenizer()
    full_prompt = f"Genre: {genre}. Story: {prompt}"

    inputs = tokenizer.encode(full_prompt, return_tensors="pt", max_length=512, truncation=True)

    outputs = model.generate(
        inputs,
        max_length=300,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9
    )

    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok", "message": "API is live"}

@app.post("/api/v1/generate", response_model=StoryResponse)
def generate_story(request: StoryRequest):
    try:
        story = generate_story_text(request.prompt.strip(), request.genre.strip() if request.genre else "general")
        return StoryResponse(story=story)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Story generation failed: {str(e)}")
