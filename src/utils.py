import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    """Mencetak pesan informasi ke log."""
    logging.info(message)

def log_error(message):
    """Mencetak pesan kesalahan ke log."""
    logging.error(message)

def validate_command(command):
    """Validasi perintah yang diberikan oleh pengguna."""
    if not command:
        return False
    # Tambahkan logika validasi tambahan jika diperlukan
    return True

def format_output(output):
    """Format output untuk ditampilkan ke pengguna."""
    return output.strip() if output else "Tidak ada output yang dihasilkan."
