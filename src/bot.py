import subprocess
from transformers import AutoModelForCausalLM, AutoTokenizer

class AILlamaBot:
    def __init__(self, model_name="model/llama"):  # Ganti dengan path model yang sesuai
        # Muat model dan tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def execute_command(self, command):
        """Eksekusi perintah sistem dan kembalikan hasilnya."""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)

    def chat(self, user_input):
        """Proses input pengguna dan kembalikan respons dari model."""
        # Tokenisasi input pengguna
        inputs = self.tokenizer.encode(user_input, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=50)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Eksekusi perintah jika ada
        if "execute:" in response:
            command = response.split("execute:")[1].strip()
            return self.execute_command(command)

        return response

def main():
    bot = AILlamaBot()
    print("Selamat datang di AI Llama Bot! Ketik 'exit' untuk keluar.")
    
    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Keluar dari bot. Terima kasih!")
            break
        bot_response = bot.chat(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
