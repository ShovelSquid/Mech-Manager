# missions to send mechs on; time, resources, enemies, skillsets




class Mission:
    def __init__(self, name, difficulty, duration, rewards):
        self.name = name
        self.difficulty = difficulty
        self.duration = duration  # in hours
        self.rewards = rewards  # dict of reward types and amounts

missionTypes = {
    "recon": {
        "description": "Scout an area and gather intel.",
        "skills": ["observation"],
    },
    "elimination": {
        "description": "Engage hostile forces.",
        "skills": ["combat"],
    },
    "escort": {
        "description": "Protect a convoy or individual.",
        "skills": ["combat", "observation"],
    },
    "rescue": {
        "description": "Rescue hostages or stranded personnel.",
        "skills": ["combat", "stealth"],
    },
    "assault": {
        "description": "Attack and capture a fortified position.",
        "skills": ["combat", "engineering"],
    },
    "defense": {
        "description": "Defend a location against waves of enemies.",
        "skills": ["combat", "engineering"],
    },
    "salvage": {
        "description": "Recover valuable materials from a dangerous area.",
        "skills": ["labor", "engineering"],
    },
    "mining": {
        "description": "Extract resources from a designated site.",
        "skills": ["labor", "engineering"],
    },
    "construction": {
        "description": "Build or repair structures in the field.",
        "skills": ["labor", "engineering"],
    }
}


# combat, stealth, labor, engineering, observation