
from pathlib import Path
from src.agents.coordinator import run_travel_planner


def main():
    print("=" * 45)
    print("RULE-BASED TRAVEL PLANNER")
    print("=" * 45)

    # Get destination
    destination = input("\nDestination: ").strip()

    if not destination:
        print("Error: Destination cannot be empty.")
        return

    # Get trip duration and number of travelers
    try:
        days = int(input("Number of days: "))
        travelers = int(input("Number of travelers: "))
    except ValueError:
        print("Error: Enter whole numbers for days and travelers.")
        return

    # Get travel style
    travel_style = input(
        "Travel style (budget/standard/premium): "
    ).strip().lower()

    # Run all agents through the coordinator
    result = run_travel_planner(
        destination,
        days,
        travelers,
        travel_style
    )

    # Handle unsuccessful results
    if not result["success"]:
        print("\nError:", result["message"])

        if "available_destinations" in result:
            print("\nAvailable destinations:")
            for name in result["available_destinations"]:
                print("-", name)

        return

    # Extract the results from each agent
    destination_info = result["destination"]
    budget = result["budget"]
    itinerary = result["itinerary"]

    # Display destination information
    print("\n" + "=" * 45)
    print("DESTINATION INFORMATION")
    print("=" * 45)

    print(f"Destination: {destination_info['destination']}")
    print(f"Region: {destination_info['region']}")

    print("\nPlaces to visit:")
    for place in destination_info["places"]:
        print(f"- {place}")

    print("\nSuggested activities:")
    for activity in destination_info["activities"]:
        print(f"- {activity}")

    # Display the itinerary
    print("\n" + "=" * 45)
    print("DAY-BY-DAY ITINERARY")
    print("=" * 45)

    for item in itinerary["itinerary"]:
        print(f"\nDay {item['day']}: {item['place']}")
        print(f"Activity: {item['activity']}")

    # Display the budget
    print("\n" + "=" * 45)
    print("ESTIMATED TRIP BUDGET")
    print("=" * 45)

    print(f"Travelers: {budget['travelers']}")
    print(f"Duration: {budget['days']} days")
    print(f"Travel style: {budget['travel_style']}")
    print(f"Transport: PKR {budget['transport']:,}")
    print(f"Hotel: PKR {budget['hotel']:,}")
    print(f"Food: PKR {budget['food']:,}")
    print(f"Activities: PKR {budget['activities']:,}")
    print(
        f"Emergency allowance: PKR {budget['contingency']:,}"
    )
    print("-" * 30)
    print(f"TOTAL ESTIMATE: PKR {budget['total']:,}")

    print("\nNote: These are example estimates, not live prices.")

    # Save the complete travel plan
    try:
        output_folder = Path("data/reports")
        output_folder.mkdir(parents=True, exist_ok=True)

        report_lines = [
            "=" * 45,
            f"TRAVEL PLAN: {destination_info['destination']}",
            "=" * 45,
            f"Region: {destination_info['region']}",
            f"Duration: {budget['days']} days",
            f"Travelers: {budget['travelers']}",
            f"Travel style: {budget['travel_style']}",
            "",
            "PLACES TO VISIT:",
        ]

        for place in destination_info["places"]:
            report_lines.append(f"- {place}")

        report_lines.extend(["", "SUGGESTED ACTIVITIES:"])

        for activity in destination_info["activities"]:
            report_lines.append(f"- {activity}")

        report_lines.extend(["", "DAY-BY-DAY ITINERARY:"])

        for item in itinerary["itinerary"]:
            report_lines.append(
                f"Day {item['day']}: {item['place']}"
            )
            report_lines.append(f"Activity: {item['activity']}")
            report_lines.append("")

        report_lines.extend([
            "=" * 45,
            "ESTIMATED TRIP BUDGET",
            "=" * 45,
            f"Transport: PKR {budget['transport']:,}",
            f"Hotel: PKR {budget['hotel']:,}",
            f"Food: PKR {budget['food']:,}",
            f"Activities: PKR {budget['activities']:,}",
            f"Emergency allowance: PKR {budget['contingency']:,}",
            "-" * 30,
            f"TOTAL ESTIMATE: PKR {budget['total']:,}",
            "",
            "Note: Estimates are illustrative, not live prices.",
        ])

        # Make a safe filename from the destination
        safe_name = "".join(
            character if character.isalnum() or character in "-_"
            else "_"
            for character in destination_info["destination"]
        ).strip("_")

        report_file = (
            output_folder / f"{safe_name}_travel_plan.txt"
        )

        report_file.write_text(
            "\n".join(report_lines),
            encoding="utf-8"
        )

        print(f"\nTravel plan saved to: {report_file}")

    except OSError as error:
        print(f"\nCould not save the travel plan: {error}")


if __name__ == "__main__":
    main()