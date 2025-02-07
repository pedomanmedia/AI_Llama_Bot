from transformers import AutoModelForCausalLM, AutoTokenizer

class ModelLoader:
    def __init__(self, model_name="model/llama"):  # Ganti dengan path model yang sesuai
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.load_model()

    def load_model(self):
        """Memuat model dan tokenizer dari path yang diberikan."""
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
            print(f"Model dan tokenizer berhasil dimuat dari {self.model_name}.")
        except Exception as e:
            print(f"Gagal memuat model: {e}")

    def get_model(self):
        """Mengembalikan model yang dimuat."""
        return self.model

    def get_tokenizer(self):
        """Mengembalikan tokenizer yang dimuat."""
        return self.tokenizer
