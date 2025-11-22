import os
import json
from datetime import datetime
from modules import player_story, timeline

DATA_DIR = "data"
PLAYER_DIR = os.path.join(DATA_DIR, "players")

# --- Utility Functions ---
def load_json_file(filepath):
    """Load JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(filepath, data):
    """Save JSON file to disk."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with ope
