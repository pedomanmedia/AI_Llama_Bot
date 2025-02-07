from command_executor import execute_command
from model_loader import ModelLoader
from utils import log_info, log_error, format_output, validate_command

class AILlamaBot:
    def __init__(self, model_name="model/llama"):  # Ganti dengan path model yang sesuai
        # Muat model dan tokenizer menggunakan ModelLoader
        model_loader = ModelLoader(model_name)
        self.tokenizer = model_loader.get_tokenizer()
        self.model = model_loader.get_model()

    def chat(self, user_input):
        """Proses input pengguna dan kembalikan respons dari model."""
        if not validate_command(user_input):
            log_error("Perintah tidak valid.")
            return "Perintah tidak valid."

        # Tokenisasi input pengguna
        inputs = self.tokenizer.encode(user_input, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=50)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Eksekusi perintah jika ada
        if "execute:" in response:
            command = response.split("execute:")[1].strip()
            output = execute_command(command)
            return format_output(output)

        return format_output(response)

def main():
    bot = AILlamaBot()
    log_info("Bot dimulai. Selamat datang di AI Llama Bot! Ketik 'exit' untuk keluar.")
    
    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["exit", "quit"]:
            log_info("Pengguna keluar dari bot.")
            print("Keluar dari bot. Terima kasih!")
            break
        bot_response = bot.chat(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
