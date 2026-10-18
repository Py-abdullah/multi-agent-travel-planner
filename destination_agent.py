
DESTINATIONS = {
    "lahore": {
        "name": "Lahore",
        "region": "Punjab, Pakistan",
        "places": [
            "Lahore Fort",
            "Badshahi Mosque",
            "Shalimar Gardens",
            "Lahore Food Street",
        ],
        "activities": [
            "Historical sightseeing",
            "Food exploration",
            "Cultural experiences",
        ],
    },
    "islamabad": {
        "name": "Islamabad",
        "region": "Islamabad Capital Territory, Pakistan",
        "places": [
            "Faisal Mosque",
            "Pakistan Monument",
            "Daman-e-Koh",
            "Rawal Lake",
        ],
        "activities": [
            "Landmark sightseeing",
            "Scenic viewpoints",
            "Parks and nature",
        ],
    },
    "murree": {
        "name": "Murree",
        "region": "Punjab, Pakistan",
        "places": [
            "Mall Road",
            "Kashmir Point",
            "Pindi Point",
            "Patriata",
        ],
        "activities": [
            "Mountain scenery",
            "Shopping on Mall Road",
            "Scenic viewpoints",
        ],
    },
    "hunza": {
        "name": "Hunza Valley",
        "region": "Gilgit-Baltistan, Pakistan",
        "places": [
            "Baltit Fort",
            "Altit Fort",
            "Attabad Lake",
            "Passu Cones",
        ],
        "activities": [
            "Mountain scenery",
            "Historical forts",
            "Photography",
        ],
    },
    "skardu": {
        "name": "Skardu",
        "region": "Gilgit-Baltistan, Pakistan",
        "places": [
            "Shangrila Resort area",
            "Upper Kachura Lake",
            "Shigar Fort",
            "Katpana Desert",
        ],
        "activities": [
            "Lake visits and landscapes",
            "Historical sightseeing",
            "Photography",
        ],
    },
    "swat": {
        "name": "Swat Valley",
        "region": "Khyber Pakhtunkhwa, Pakistan",
        "places": [
            "Mingora",
            "Malam Jabba",
            "Swat Museum",
            "Fizagat Park",
        ],
        "activities": [
            "Valley sightseeing",
            "Mountain scenery",
            "Cultural experiences",
        ],
    },
}


def destination_agent(destination: str) -> dict:
    """Find destination information using a local database."""

    if not isinstance(destination, str) or not destination.strip():
        return {
            "success": False,
            "message": "Please enter a valid destination name.",
            "available_destinations": [
                data["name"] for data in DESTINATIONS.values()
            ],
        }

    key = destination.strip().lower()

    # Map alternative names to their database keys.
    aliases = {
        "lahore city": "lahore",
        "islamabad capital territory": "islamabad",
        "murree hills": "murree",
        "hunza valley": "hunza",
        "skardu valley": "skardu",
        "swat valley": "swat",
    }

    key = aliases.get(key, key)

    if key not in DESTINATIONS:
        return {
            "success": False,
            "message": (
                f"Sorry, {destination} is not in our "
                "destination database yet."
            ),
            "available_destinations": [
                data["name"] for data in DESTINATIONS.values()
            ],
        }

    data = DESTINATIONS[key]

    return {
        "success": True,
        "destination": data["name"],
        "region": data["region"],
        "places": data["places"],
        "activities": data["activities"],
    }