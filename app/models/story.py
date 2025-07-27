from pydantic import BaseModel, Field
from typing import Optional


class StoryRequest(BaseModel):
    prompt: str = Field(..., example="A lonely robot exploring Mars")
    genre: Optional[str] = Field("sci-fi", example="sci-fi", description="Optional story genre")

    class Config:
        schema_extra = {
            "example": {
                "prompt": "A young girl discovers she can speak to animals",
                "genre": "fantasy"
            }
        }


class StoryResponse(BaseModel):
    story: str = Field(..., example="Once upon a time in a mystical forest...")

    class Config:
        schema_extra = {
            "example": {
                "story": "Once upon a time in a mystical forest, a young girl named Lyra discovered she could speak to animals..."
            }
        }
