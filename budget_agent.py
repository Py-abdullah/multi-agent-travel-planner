
def budget_agent(destination: str, days: int, travelers: int, travel_style: str) -> dict:
    """Estimate a trip budget using predefined daily costs in PKR."""

    if days < 1 or days > 30:
        return {"success": False, "message": "Days must be between 1 and 30."}

    if travelers < 1 or travelers > 20:
        return {"success": False, "message": "Travelers must be between 1 and 20."}

    # Approximate per-person daily costs in Pakistani rupees.
    # These are example estimates, not live prices.
    daily_costs = {
        "budget": {
            "transport": 1500,
            "hotel": 1500,
            "food": 1200,
            "activities": 500,
        },
        "standard": {
            "transport": 2500,
            "hotel": 3500,
            "food": 2000,
            "activities": 1000,
        },
        "premium": {
            "transport": 5000,
            "hotel": 8000,
            "food": 3500,
            "activities": 2500,
        },
    }

    style = travel_style.strip().lower()

    if style not in daily_costs:
        return {
            "success": False,
            "message": "Travel style must be budget, standard, or premium.",
        }

    costs = daily_costs[style]

    # Estimate the cost for all travelers and all days.
    transport_total = costs["transport"] * travelers * days
    hotel_total = costs["hotel"] * travelers * days
    food_total = costs["food"] * travelers * days
    activities_total = costs["activities"] * travelers * days

    subtotal = (
        transport_total
        + hotel_total
        + food_total
        + activities_total
    )

    contingency = round(subtotal * 0.10)
    total = subtotal + contingency

    return {
        "success": True,
        "destination": destination.title(),
        "days": days,
        "travelers": travelers,
        "travel_style": style.title(),
        "transport": transport_total,
        "hotel": hotel_total,
        "food": food_total,
        "activities": activities_total,
        "contingency": contingency,
        "total": total,
        "currency": "PKR",
    }