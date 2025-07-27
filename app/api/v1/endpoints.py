from fastapi import APIRouter, HTTPException
from app.models.story import StoryRequest, StoryResponse
from app.services.story_generator import generate_story

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify the API is up.
    """
    return {"status": "ok", "message": "Story Maker API is running."}


@router.post("/generate", response_model=StoryResponse, tags=["Story Generation"])
def generate_story_endpoint(request: StoryRequest):
    """
    Generate a story based on user prompt and genre.
    """
    try:
        response = generate_story(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Story generation failed: {str(e)}")


@router.get("/examples", tags=["Examples"])
def example_prompts():
    """
    Provide example prompts to the user.
    """
    return {
        "examples": [
            {"prompt": "A young girl discovers a hidden portal in her backyard", "genre": "fantasy"},
            {"prompt": "A detective investigates a series of strange disappearances", "genre": "mystery"},
            {"prompt": "Aliens make first contact with Earth in 2093", "genre": "sci-fi"},
        ]
    }


@router.get("/", tags=["Info"])
def welcome():
    """
    Welcome endpoint.
    """
    return {
        "message": "Welcome to the AI Story Maker API!",
        "endpoints": ["/health", "/generate", "/examples"],
        "version": "v1"
    }
