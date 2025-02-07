import unittest
from unittest.mock import patch, MagicMock
from src.command_executor import execute_command

class TestCommandExecutor(unittest.TestCase):

    @patch('subprocess.run')
    def test_execute_command_success(self, mock_run):
        # Siapkan mock untuk subprocess.run
        mock_run.return_value = MagicMock(returncode=0, stdout='file1.txt\nfile2.txt', stderr='')

        # Uji eksekusi perintah yang berhasil
        command = "ls"
        result = execute_command(command)
        self.assertEqual(result, 'file1.txt\nfile2.txt')
        mock_run.assert_called_once_with(command, shell=True, capture_output=True, text=True)

    @patch('subprocess.run')
    def test_execute_command_failure(self, mock_run):
        # Siapkan mock untuk subprocess.run yang gagal
        mock_run.return_value = MagicMock(returncode=1, stdout='', stderr='Error: Command not found')

        # Uji eksekusi perintah yang gagal
        command = "invalid_command"
        result = execute_command(command)
        self.assertEqual(result, 'Error: Command not found')
        mock_run.assert_called_once_with(command, shell=True, capture_output=True, text=True)

    @patch('subprocess.run')
    def test_execute_command_exception(self, mock_run):
        # Siapkan mock untuk menimbulkan exception
        mock_run.side_effect = Exception("An error occurred")

        # Uji eksekusi perintah yang menimbulkan exception
        command = "ls"
        result = execute_command(command)
        self.assertEqual(result, "An error occurred")
        mock_run.assert_called_once_with(command, shell=True, capture_output=True, text=True)

if __name__ == '__main__':
    unittest.main()
