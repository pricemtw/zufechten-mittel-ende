# modules/event_templates.py

def combat_event_template(player_name, npc_name, area, objects=None, outcome="", description="", tone="serious"):
    return {
        "type": "combat",
        "player": player_name,
        "npc": npc_name,
        "world_area": area,
        "related_objects": objects or [],
        "description": description,
        "outcome": outcome,
        "consequence": {},
        "tone": tone
    }

def exploration_event_template(player_name, area, objects=None, description="", tone="neutral"):
    return {
        "type": "exploration",
        "player": player_name,
        "world_area": area,
        "related_objects": objects or [],
        "description": description,
        "outcome": "",
        "consequence": {},
        "tone": tone
    }

def item_event_template(player_name, item_name, area, description="", tone="neutral"):
    return {
        "type": "item",
        "player": player_name,
        "world_area": area,
        "related_objects": [item_name],
        "description": description,
        "outcome": "",
        "consequence": {},
        "tone": tone
    }
