from app.ml.model_loader import ModelLoader
import torch

_model_loader = None

def get_model_loader():
    global _model_loader
    if _model_loader is None:
        _model_loader = ModelLoader("mosaicml/mpt-7b-storywriter")
        _model_loader.load()
    return _model_loader

def generate_story(prompt: str, max_length: int = 500, temperature: float = 0.8,
                   top_k: int = 50, top_p: float = 0.95) -> str:
    model_loader = get_model_loader()
    tokenizer = model_loader.get_tokenizer()
    model = model_loader.get_model()

    device = model_loader.device

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.eos_token_id
        )
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story
