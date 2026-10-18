
from src.agents.destination_agent import destination_agent
from src.agents.budget_agent import budget_agent
from src.agents.itinerary_agent import itinerary_agent


def run_travel_planner(
    destination: str,
    days: int,
    travelers: int,
    travel_style: str
) -> dict:
    """Coordinate the destination, budget, and itinerary agents."""

    # Agent 1: Find destination information.
    destination_info = destination_agent(destination)

    if not destination_info["success"]:
        return destination_info

    # Agent 2: Estimate the travel budget.
    budget_info = budget_agent(
        destination_info["destination"],
        days,
        travelers,
        travel_style
    )

    if not budget_info["success"]:
        return budget_info

    # Agent 3: Generate the itinerary.
    itinerary_info = itinerary_agent(
        destination_info["destination"],
        days
    )

    if not itinerary_info["success"]:
        return itinerary_info

    # Combine all agent results.
    return {
        "success": True,
        "destination": destination_info,
        "budget": budget_info,
        "itinerary": itinerary_info
    }