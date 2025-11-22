def validate_event_coherence(event, player_data, world_data, story_data):
    """
    Check if the new event is consistent with:
    - Player inventory and past actions
    - World state
    - Timeline / global events
    Returns True if event can proceed.
    """
    # Example: player can't pick up an item already claimed
    if "item" in event:
        for past_event in story_data.values():
            if event["item"] in past_event.get("related_objects", []):
                return False
    return True
