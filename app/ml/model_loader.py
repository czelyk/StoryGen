from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class ModelLoader:
    def __init__(self, model_name: str, device: str = None):
        """
        Modeli ve tokenizer'ı yükler.

        Args:
            model_name (str): Hugging Face model adı veya yolu.
            device (str, optional): 'cuda' veya 'cpu'. Otomatik tespit edilir.
        """
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = None
        self.model = None

    def load(self):
        print(f"Loading model '{self.model_name}' on device '{self.device}'...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None,
        )
        self.model.eval()
        print("Model loaded successfully.")

    def get_tokenizer(self):
        if self.tokenizer is None:
            raise ValueError("Model not loaded yet. Call load() first.")
        return self.tokenizer

    def get_model(self):
        if self.model is None:
            raise ValueError("Model not loaded yet. Call load() first.")
        return self.model
