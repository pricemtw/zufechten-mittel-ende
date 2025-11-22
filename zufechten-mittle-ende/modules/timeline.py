import os
import json
from datetime import datetime

DATA_DIR = "data"
TIMELINE_FILE = os.path.join(DATA_DIR, "timeline.json")

# --- Utility Functions ---
def load_json_file(filepath):
    """Load a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(filepath, data):
    """Save JSON file to disk."""
    os.makedirs(os.path.dirname(filepath), ex
