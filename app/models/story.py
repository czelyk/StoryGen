from pydantic import BaseModel, Field
from typing import Optional

class StoryRequest(BaseModel):
    prompt: str = Field(..., example="A young girl discovers a hidden portal in her backyard.")
    genre: Optional[str] = Field("general", example="fantasy")

class StoryResponse(BaseModel):
    story: str = Field(..., example="Once upon a time, in a land far away...")
