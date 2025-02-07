from transformers import AutoModelForCausalLM

model_name = "huggingface/llama"  # Ganti dengan nama model yang sesuai
model = AutoModelForCausalLM.from_pretrained(model_name)
model.save_pretrained("models/llama_model")
