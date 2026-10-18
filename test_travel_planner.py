
import unittest

from src.agents.destination_agent import destination_agent
from src.agents.budget_agent import budget_agent
from src.agents.itinerary_agent import itinerary_agent
from src.agents.coordinator import run_travel_planner


class TestTravelPlanner(unittest.TestCase):

    def test_valid_destination(self):
        result = destination_agent("Hunza Valley")
        self.assertTrue(result["success"])

    def test_invalid_destination(self):
        result = destination_agent("Atlantis")
        self.assertFalse(result["success"])

    def test_valid_budget(self):
        result = budget_agent("Hunza Valley", 3, 2, "budget")
        self.assertTrue(result["success"])
        self.assertGreater(result["total"], 0)

    def test_invalid_days(self):
        result = budget_agent("Hunza", 0, 2, "budget")
        self.assertFalse(result["success"])

    def test_invalid_travel_style(self):
        result = budget_agent("Hunza", 3, 2, "luxury")
        self.assertFalse(result["success"])

    def test_itinerary_length(self):
        result = itinerary_agent("Hunza Valley", 3)
        self.assertTrue(result["success"])
        self.assertEqual(len(result["itinerary"]), 3)

    def test_complete_travel_plan(self):
        result = run_travel_planner(
            "Hunza Valley", 3, 2, "budget"
        )
        self.assertTrue(result["success"])


if __name__ == "__main__":
    unittest.main()
