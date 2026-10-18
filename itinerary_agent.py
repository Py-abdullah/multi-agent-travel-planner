
from src.agents.destination_agent import destination_agent


def itinerary_agent(destination: str, days: int) -> dict:
    """Create a simple day-by-day itinerary using predefined destination data."""

    if days < 1 or days > 30:
        return {
            "success": False,
            "message": "Days must be between 1 and 30."
        }

    destination_data = destination_agent(destination)

    if not destination_data["success"]:
        return {
            "success": False,
            "message": destination_data["message"]
        }

    places = destination_data["places"]
    activities = destination_data["activities"]

    itinerary = []

    for day in range(1, days + 1):
        place = places[(day - 1) % len(places)]
        activity = activities[(day - 1) % len(activities)]

        itinerary.append({
            "day": day,
            "place": place,
            "activity": activity
        })

    return {
        "success": True,
        "destination": destination_data["destination"],
        "days": days,
        "itinerary": itinerary
    }