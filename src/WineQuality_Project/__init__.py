import logging
import os
from datetime import datetime

# -----------------------------
# Create logs directory
# -----------------------------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# -----------------------------
# Log file with timestamp
# -----------------------------
log_file = os.path.join(LOG_DIR, f"project_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# -----------------------------
# Logger setup
# -----------------------------
logger = logging.getLogger("WineQualityLogger")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

# Stream handler (terminal)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
