# Multi-Agent Travel Planner

A Python-based travel planning application that coordinates multiple specialized agents to generate destination recommendations, estimate trip budgets, and create day-by-day itineraries.

## Features

- **Destination Agent:** Provides destination information, attractions, and activities.
- **Budget Agent:** Estimates trip expenses based on duration, number of travelers, and travel style.
- **Itinerary Agent:** Generates a daily itinerary for the selected destination.
- **Coordinator Agent:** Combines the agents to produce a complete travel plan.
- **Streamlit Web Interface:** Allows users to enter trip details through a web page.
- **Travel Report:** Saves the generated plan as a downloadable text file.
- **Input Validation:** Handles invalid destinations and trip details.
- **Automated Tests:** Includes unit tests for core functionality.

## Supported Destinations

- Lahore
- Islamabad
- Murree
- Hunza Valley
- Skardu
- Swat Valley

## Technologies Used

- Python
- Streamlit
- Unit Testing (`unittest`)
- GitHub

## Project Structure

```text
multi-agent-system/
├── app.py
├── travel_planner.py
├── main.py
├── test_travel_planner.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   └── agents/
│       ├── coordinator.py
│       ├── destination_agent.py
│       ├── budget_agent.py
│       └── itinerary_agent.py
├── data/
│   └── reports/
└── logs/
```

## Installation

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Web Application

Start the Streamlit interface:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Run the Command-Line Version

```bash
python travel_planner.py
```

## Run the Tests

```bash
python -m unittest test_travel_planner.py -v
```

## Budget Disclaimer

Budget figures are illustrative estimates, not live prices or confirmed travel costs. Actual expenses depend on transportation, accommodation, season, and personal preferences.

## Future Improvements

- Live hotel and transportation prices
- Weather and travel information integration
- More destinations and customizable activities
- Improved budget calculations and accommodation sharing
- More comprehensive automated testing

## Author

**Abdullah Musa**

---

*This project is a learning project exploring Python application development and multi-agent system design.*
