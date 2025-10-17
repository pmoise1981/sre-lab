import qrcode
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def generate_qr(url, filename):
    """Generate a QR code and save it."""
    qr = qrcode.make(url)
    qr.save(filename)
    logger.info(f"QR code saved as {filename}")

if __name__ == "__main__":
    url = os.getenv("QR_URL", "https://github.com/pmoise1981")
    filename = os.getenv("QR_FILENAME", "github_qr.png")
    
    logger.info(f"Generating QR Code for {url}")
    generate_qr(url, filename)

