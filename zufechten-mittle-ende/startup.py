import os
import json
from modules import player, world_state, player_story, timeline

# Base paths
DATA_DIR = "data"
PLAYER_DIR = os.path.join(DATA_DIR, "players")
WORLD_DIR = os.path.join(DATA_DIR, "world")
STORY_DIR = os.path.join(DATA_DIR, "story")

# Chunk size (for large files)
CHUNK_SIZE = 50 * 1024  # 50KB

# Utility functions
def load_json_file(filepath):
    """Load a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(filepath, data):
    """Save JSON file to disk."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_chunked_file(base_path):
    """Load all chunked files for a given base path and merge into one dict."""
    data = {}
    if not os.path.exists(base_path):
        return data

    for filename in sorted(os.listdir(base_path)):
        if filename.startswith(os.path.basename(base_path)):
            chunk_path = os.path.join(base_path, filename)
            chunk_data = load_json_file(chunk_path)
            data.update(chunk_data)
    return data

# Main startup
def main():
    print("Welcome to Zufechten, Mittel, Ende!")
    
    # --- Load or create player ---
    player_name = input("Enter your player name: ").strip()
    player_file = os.path.join(PLAYER_DIR, f"{player_name}.json")
    if os.path.exists(player_file):
        print(f"Resuming player {player_name}...")
        player_data = load_json_file(player_file)
    else:
        print(f"Creating new player {player_name}...")
        player_data = player.create_new_player(player_name)
        save_json_file(player_file, player_data)
    
    # --- Load world state ---
    world_data = load_chunked_file(WORLD_DIR)
    print(f"Loaded world with {len(world_data)} chunks.")
    
    # --- Load story summary ---
    story_data = load_chunked_file(STORY_DIR)
    print(f"Loaded story summary with {len(story_data)} entries.")
    
    # --- Load timeline ---
    timeline_file = os.path.join(DATA_DIR, "timeline.json")
    timeline_data = load_json_file(timeline_file)
    
    # Main loop placeholder
    while True:
        print("\n--- Main Menu ---")
        print("1. Explore")
        print("2. Check Player Status")
        print("3. View Timeline")
        print("4. Save & Exit")
        choice = input("> ").strip()
        
        if choice == "1":
            # Placeholder: call world_state exploration
            world_state.explore(player_data, world_data, story_data, timeline_data)
        elif choice == "2":
            player.show_status(player_data)
        elif choice == "3":
            timeline.show_timeline(timeline_data)
        elif choice == "4":
            # Save everything
            save_json_file(player_file, player_data)
            save_json_file(timeline_file, timeline_data)
            print("Game saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
