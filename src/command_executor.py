import subprocess

def execute_command(command):
    """Eksekusi perintah sistem dan kembalikan hasilnya."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
