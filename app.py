
import streamlit as st
from pathlib import Path
from src.agents.coordinator import run_travel_planner


# Page configuration
st.set_page_config(
    page_title="Travel Planner | Pakistan",
    page_icon="✈️",
    layout="wide",
)


# Page heading
st.title("✈️ Pakistan Travel Planner")
st.write(
    "Plan your trip, explore destinations, "
    "view a daily itinerary, and estimate your budget."
)

st.info(
    "This application uses predefined destination data "
    "and illustrative budget estimates. It does not use live prices."
)


# Sidebar: Trip preferences
st.sidebar.header("Plan Your Trip")

destinations = [
    "Lahore",
    "Islamabad",
    "Murree",
    "Hunza Valley",
    "Skardu",
    "Swat Valley",
]

destination = st.sidebar.selectbox(
    "Choose your destination",
    destinations,
)

days = st.sidebar.number_input(
    "Trip duration (days)",
    min_value=1,
    max_value=30,
    value=3,
    step=1,
)

travelers = st.sidebar.number_input(
    "Number of travelers",
    min_value=1,
    max_value=20,
    value=2,
    step=1,
)

travel_style = st.sidebar.selectbox(
    "Travel style",
    ["budget", "standard", "premium"],
)

st.sidebar.caption(
    "Budget estimates are calculated using example rates."
)


# Generate the travel plan
if st.button("Generate My Travel Plan", type="primary"):
    with st.spinner("Preparing your travel plan..."):
        try:
            result = run_travel_planner(
                destination,
                int(days),
                int(travelers),
                travel_style,
            )

            if not result.get("success"):
                st.error(result.get("message", "Could not generate the plan."))

                available = result.get("available_destinations")
                if available:
                    st.write("Available destinations:", ", ".join(available))

            else:
                destination_info = result["destination"]
                budget = result["budget"]
                itinerary = result["itinerary"]

                # Destination overview
                st.success("Your travel plan is ready!")

                st.header(
                    f"Your Trip to {destination_info['destination']}"
                )
                st.write(f"**Region:** {destination_info['region']}")

                first_col, second_col, third_col = st.columns(3)

                first_col.metric("Duration", f"{days} days")
                second_col.metric("Travelers", int(travelers))
                third_col.metric(
                    "Estimated Total",
                    f"PKR {budget['total']:,}",
                )

                # Places and activities
                st.subheader("📍 Places to Visit")

                st.write(" · ".join(destination_info["places"]))

                st.subheader("🌿 Suggested Activities")

                for activity in destination_info["activities"]:
                    st.write(f"- {activity}")

                # Itinerary
                st.subheader("🗓️ Day-by-Day Itinerary")

                for item in itinerary["itinerary"]:
                    with st.expander(
                        f"Day {item['day']} — {item['place']}",
                        expanded=True,
                    ):
                        st.write(f"**Activity:** {item['activity']}")

                # Budget breakdown
                st.subheader("💰 Estimated Budget")

                budget_col1, budget_col2 = st.columns(2)

                with budget_col1:
                    st.write("**Expense category**")
                    st.write("Transportation")
                    st.write("Accommodation")
                    st.write("Food")
                    st.write("Activities")
                    st.write("Emergency allowance")
                    st.divider()
                    st.write("**Total estimate**")

                with budget_col2:
                    st.write("**Estimated cost (PKR)**")
                    st.write(f"{budget['transport']:,}")
                    st.write(f"{budget['hotel']:,}")
                    st.write(f"{budget['food']:,}")
                    st.write(f"{budget['activities']:,}")
                    st.write(f"{budget['contingency']:,}")
                    st.divider()
                    st.write(f"**PKR {budget['total']:,}**")

                # Prepare a downloadable report
                report_lines = [
                    f"TRAVEL PLAN: {destination_info['destination']}",
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

                report_lines.extend(["", "ITINERARY:"])

                for item in itinerary["itinerary"]:
                    report_lines.append(
                        f"Day {item['day']}: {item['place']}"
                    )
                    report_lines.append(
                        f"Activity: {item['activity']}"
                    )
                    report_lines.append("")

                report_lines.extend([
                    "BUDGET BREAKDOWN:",
                    f"Transport: PKR {budget['transport']:,}",
                    f"Accommodation: PKR {budget['hotel']:,}",
                    f"Food: PKR {budget['food']:,}",
                    f"Activities: PKR {budget['activities']:,}",
                    f"Emergency allowance: PKR {budget['contingency']:,}",
                    f"TOTAL: PKR {budget['total']:,}",
                    "",
                    "Note: These are illustrative estimates, not live prices.",
                ])

                report_text = "\n".join(report_lines)

                safe_name = "".join(
                    char if char.isalnum() or char in "-_" else "_"
                    for char in destination_info["destination"]
                ).strip("_")

                st.download_button(
                    label="⬇️ Download Travel Plan",
                    data=report_text,
                    file_name=f"{safe_name}_travel_plan.txt",
                    mime="text/plain",
                )

                # Also save a copy in the project folder
                try:
                    reports_folder = Path("data/reports")
                    reports_folder.mkdir(
                        parents=True,
                        exist_ok=True,
                    )

                    report_path = (
                        reports_folder
                        / f"{safe_name}_travel_plan.txt"
                    )

                    report_path.write_text(
                        report_text,
                        encoding="utf-8",
                    )

                    st.caption(
                        f"Project copy saved to: {report_path}"
                    )

                except OSError as error:
                    st.warning(
                        f"The download is available, but the project "
                        f"copy could not be saved: {error}"
                    )

        except (KeyError, TypeError, ValueError) as error:
            st.error(f"Could not process the travel plan: {error}")

        except OSError as error:
            st.error(f"A file operation failed: {error}")


# Footer
st.divider()
st.caption(
    "Built with Python and Streamlit | "
    "Rule-Based Multi-Agent Travel Planner"
)