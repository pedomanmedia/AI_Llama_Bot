import unittest
from unittest.mock import patch, MagicMock
from src.bot import AILlamaBot

class TestAILlamaBot(unittest.TestCase):

    @patch('src.model_loader.ModelLoader')
    def setUp(self, MockModelLoader):
        # Siapkan model dan tokenizer palsu
        self.mock_model = MagicMock()
        self.mock_tokenizer = MagicMock()
        
        # Konfigurasi model loader palsu
        MockModelLoader.return_value.get_model.return_value = self.mock_model
        MockModelLoader.return_value.get_tokenizer.return_value = self.mock_tokenizer
        
        # Inisialisasi bot
        self.bot = AILlamaBot(model_name="model/llama")

    def test_chat_valid_command(self):
        # Siapkan input dan output palsu
        user_input = "Hello"
        self.mock_tokenizer.encode.return_value = [1, 2, 3]
        self.mock_model.generate.return_value = [[4, 5, 6]]
        self.mock_tokenizer.decode.return_value = "execute: ls"

        # Uji respons bot
        response = self.bot.chat(user_input)
        self.assertEqual(response, "execute: ls")

    @patch('src.command_executor.execute_command')
    def test_chat_execute_command(self, mock_execute_command):
        # Siapkan input dan output palsu
        user_input = "List files"
        self.mock_tokenizer.encode.return_value = [1, 2, 3]
        self.mock_model.generate.return_value = [[4, 5, 6]]
        self.mock_tokenizer.decode.return_value = "execute: ls"
        
        # Siapkan hasil eksekusi perintah
        mock_execute_command.return_value = "file1.txt\nfile2.txt"

        # Uji respons bot saat mengeksekusi perintah
        response = self.bot.chat(user_input)
        self.assertEqual(response, "file1.txt\nfile2.txt")

    def test_chat_invalid_command(self):
        # Uji respons bot untuk perintah tidak valid
        user_input = ""
        response = self.bot.chat(user_input)
        self.assertEqual(response, "Perintah tidak valid.")

if __name__ == '__main__':
    unittest.main()
